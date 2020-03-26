.. _overview:

Overview 
============================================

In order to facilitate the integration of data between `OpenEdition Books <https://books.openedition.org>`_,
`OpenEdition Journals <https://journals.openedition.org>`_, knowledge bases and
discovery tools, KBART metadata (`Knowledge Base And Related Tools <https://www.niso.org/standards-committees/kbart>`_)
is now available for download on `OpenEdition <https://www.openedition.org/title-list>`_
and `BACON <https://bacon.abes.fr/exporter.html>`_, the French national knowledge
base (BAse de COnnaissance Nationale Française). Such data provides information
relating to the status of the collections and the bundles available for purchase.

KBART files are published on BACON under the `CC0 license <https://creativecommons.org/publicdomain/zero/1.0/deed>`_
and on OpenEdition under the following licenses: `Creative Commons Attribution 4.0 International License <https://creativecommons.org/licenses/by/4.0/>`_
and the French `"Licence Ouverte / Open license" <https://www.etalab.gouv.fr/licence-ouverte-open-licence>`_.

Knowledge Base And Related Tools
----------------------------------

In an era of electronic documentation, we are facing the challenge of ever-evolving
catalogues and moving resources. In order to tackle this issue, the US agency for
normalisation proposed KBART as a framework for sharing information about electronic
collections.

The KBART recommandation mostly consists of a standard 25 columns `TSV <https://en.wikipedia.org/wiki/Tab-separated_values>`_
table and best practices about how to fill it, name it and share it.
KBART files are very well suited to describe electronic collections such as 
OpenEdition's. For each available resource, it allows one to get minimal bibliographic
information along with access modalities (is this journal Open Access? what is the URL for
that book?)

Yet, the KBART format **is not** adapted to retrieve detailed metadata
about a resource. It is made to describe catalogues, bundles and states of
collections. In case you're looking for detailed metadata about OpenEdition resources,
you should consider reading OpenEdition's `OAI-PMH <https://oai-openedition.readthedocs.io/>`_
or `MARC <https://marc-openedition.readthedocs.io/en/latest/index.html>`_ documentations.
In this case, KBART could be useful as en entry point in order to retrieve
identifiers, for example. Such case is developed in the ":ref:`further`" section
of this documentation.

A standard format such as KBART facilitates interoperability, electronic
resources maintenance and subscription management. It allows one to develop or
use tools that are not provider-dependant.

.. include:: bacon.rst
