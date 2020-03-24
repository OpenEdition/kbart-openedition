.. _further:

Going further...
==================

Using the Kbart files is also an opportunity to get a bit into OpenEdition's
data.
As an example, this page will show how to retrieve structured metadata about
available issues for a given journal, using KBART files.

We will be using common command line tools to illustrate how it can be achieved
but other implementations are possible.

We'll be working on the journal identified by ISSN `2275-2145 <https://portal.issn.org/resource/ISSN/2275-2145>`_,
*Sciences de la société*

.. contents:: Table of Contents
   :depth: 2
   

Get the KBART from BACON
--------------------------------

First we need to get the data. Refer to the :ref:`access section of this documentation <access>`
in order to identify the relevant package for your case and its URL.

We use here the whole OpenEdition Journal catalogue, so the matching URL is ``https://bacon.abes.fr/package2kbart/OPENEDITION_GLOBAL_ALLJOURNALS.txt``

For this example, we will be using `curl <https://curl.haxx.se/>`_ to download
the desired KBART file:

.. code-block:: bash

   $ curl https://bacon.abes.fr/package2kbart/OPENEDITION_GLOBAL_ALLJOURNALS.txt

Extract a journal's data
--------------------------------

This last command will pour the entire catalogue description as TSV in the console
and its output won't be shown here. Instead, we'll pipe (``|``) it to `grep <https://www.gnu.org/software/grep/manual/grep.html>`_
in order to isolate the target journal, with ``grep 2275-2145``:

.. code-block:: bash

   $ curl https://bacon.abes.fr/package2kbart/OPENEDITION_GLOBAL_ALLJOURNALS.txt | grep 2275-2145
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
   100 32736    0 32736    0     0   9977      0 --:--:--  0:00:03 --:--:--  9977
   Sciences de la société	1168-1446	2275-2145	2010	79					http://journals.openedition.org/sds		sds		fulltext	Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	Presses universitaires du Midi	serial								F	180782584

Parse columns to find an identifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please refer to the :ref:`data description section of this documentation <description>`
in order to identify the relevant fields for your case.

Here, the identifier we need is in the ``target_id`` column, which happens to be the twelfth.
Then we can simply `cut <http://man7.org/linux/man-pages/man1/cut.1.html>`_ the
line to extract this identifier, with ``cut -d$'\t' -f12``:

.. code-block:: bash

   $ curl https://bacon.abes.fr/package2kbart/OPENEDITION_GLOBAL_ALLJOURNALS.txt | grep 2275-2145 | cut -d$'\t' -f12
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                  Dload  Upload   Total   Spent    Left  Speed
   100  119k    0  119k    0     0  40395      0 --:--:--  0:00:03 --:--:-- 40395
   sds

Query OAI-PMH
--------------------------------

Now we will query the OpenEdition OAI-PMH repository using this identifier.
Please refer to the `documentation <https://oai-openedition.readthedocs.io>`_ if
you need more information about it.

We will use this sample query URL from the documentation, which expects a
journal identifier to be appended to it: ``http://oai.openedition.org/?verb=ListRecords&metadataPrefix=mets&set=journals:``

So we can use the commands we already saw to append this identifier:

.. code-block:: bash

   $ curl https://bacon.abes.fr/package2kbart/OPENEDITION_GLOBAL_ALLJOURNALS.txt | grep 2275-2145 | cut -d$'\t' -f12 | curl "http://oai.openedition.org/?verb=ListRecords&metadataPrefix=mets&set=journals:$(</dev/stdin)"
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                  Dload  Upload   Total   Spent    Left  Speed
   100  119k    0  119k    0     0  35593      0 --:--:--  0:00:03 --:--:-- 35603
    <?xml version="1.0" encoding="UTF-8"?>
    <OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
      <responseDate>2020-03-24T14:51:22Z</responseDate>
      <request verb="ListRecords" metadataPrefix="mets" set="journals:sds">http://oai.openedition.org/</request>
      <ListRecords xmlns:mets="http://www.loc.gov/METS/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xlink="http://www.w3.org/1999/xlink">
        <record>
          <header>
            <identifier>oai:revues.org:sds/6800</identifier>
            <datestamp>2019-11-25T16:59:19Z</datestamp>
            <setSpec>journals</setSpec>
            <setSpec>journals:sds</setSpec>
            <setSpec>openaire</setSpec>
          </header>
          <metadata>
            <mets:mets xmlns:mets="http://www.loc.gov/METS/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd http://www.w3.org/1999/xlink http://www.loc.gov/standards/mets/xlink.xsd http://purl.org/dc/terms/ https://dublincore.org/schemas/xmls/qdc/2006/01/06/dcterms.xsd">
              <mets:dmdSec ID="MD_OJ_sds_6800">
                <mets:mdWrap MDTYPE="DC" LABEL="Dublin Core Descriptive Metadata" MIMETYPE="text/xml">
                  <mets:xmlData>
                    <dcterms:title>L'événement politique en ligne</dcterms:title>
                    <dcterms:type>issue</dcterms:type>
    [...]
    output has been truncated

We now have a XML-structured list of records, formated as Metadata Encoding and
Transmission Standard (mets), describing available issues for the journal
*Sciences de la société*, identified by ISSN 2275-2145.
