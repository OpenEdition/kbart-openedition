.. _description:

Data description
============================================

KBART-formatted files are UTF-8-encoded 25 columns `TSV <https://en.wikipedia.org/wiki/Tab-separated_values>`_
tables. The first line of a KBART file is always the header, so it must contain
the title of each field.

We will be describing here how each field is filled in OpenEdition's KBART files.
An empty implementation note means the field is never used.

+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field title                               | Implementation notes                                                                                                                                                      |
+===========================================+===========================================================================================================================================================================+
| publication_title                         | title of the described resource                                                                                                                                           |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| print_identifier                          | | if any: print ISSN for OpenEdition Journals,                                                                                                                            |
|                                           | | print ISBN for OpenEdition Books                                                                                                                                        |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| online_identifier                         | | electronic ISSN for OpenEdition Journals & Hypotheses research blogs                                                                                                    |
|                                           | | electronic ISBN for OpenEdition Books                                                                                                                                   |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| date_first_issue_online                   | | year of first available issue for OpenEdition Journals                                                                                                                  |
|                                           | | date of first post for Hypotheses Research blogs                                                                                                                        |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| num_first_vol_online                      | number of the first available volume for OpenEdition Journals                                                                                                             |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| num_first_issue_online                    | number of the first available issue for OpenEdition Journals                                                                                                              |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| date_last_issue_online                    | | year of last available issue for OpenEdition Journals (for both embargoed and inactive journals)                                                                        |
|                                           | | date of last post for inactive Hypotheses Research blogs                                                                                                                |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| num_last_vol_online                       | number of the last available volume for OpenEdition Journals                                                                                                              |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| num_last_issue_online                     | number of the last available issue for OpenEdition Journals                                                                                                               |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| title_url                                 | URL of the described resource                                                                                                                                             |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| first_author                              | first author, for OpenEdition Books                                                                                                                                       |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| title_id                                  | identifier of the described resource                                                                                                                                      |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| embargo_info                              | **Not implemented, even for embargoed journals**                                                                                                                          |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| coverage_depth                            | ``fulltext``                                                                                                                                                              |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| notes                                     | see the :ref:`notes section below<notesfield>`                                                                                                                            |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| publisher_name                            | publisher name                                                                                                                                                            |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| publication_type                          | | ``serial`` for OpenEdition Journals and Hypotheses                                                                                                                      |
|                                           | | ``monograph`` for OpenEdition Books                                                                                                                                     |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| date_monograph_published_print            | print publication date for OpenEdition Books, if any                                                                                                                      |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| date_monograph_published_online           | electronic publication date on OpenEdition Books                                                                                                                          |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| monograph_volume                          |                                                                                                                                                                           |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| monograph_edition                         |                                                                                                                                                                           |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| first_editor                              | name of the first editor for OpenEdition Books, if any                                                                                                                    |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| parent_publication_title_id               |                                                                                                                                                                           |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| preceding_publication_title_id            |                                                                                                                                                                           |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| access_type                               | | ``F`` for OpenEdition Journals, Open Access & Open Access Freemium OpenEdition Books and Hypotheses                                                                     |
|                                           | | ``P`` for exclusive access OpenEdition Books                                                                                                                            |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _notesfield:

Notes
-------

The ``notes`` field is used in order to provide complementary information which
could not expressed in the other fields.

All Open Access Freemium Journals are highlighted with this note:
``Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.``

Moreover, for OpenEdition Journals, some characters and abbreviations are used to
precisely describe coverage range:
 * ``abs.`` is used to list missing issues. For example ``abs. 2018, 12`` means issue #12 published in 2018 is missing.
 * ``suppl.`` is used to list added content, such as special issues: ``suppl. HS 2001`` means a special issue identified as "HS 2001" is available.
 * ``;`` is used as a separator between issues: ``abs. 2018, 12 ; 2019, 15`` means issues 12 and 15 are missing
 * ``—`` is used as a continuity marker: ``abs. 2018, 12—2019, 15`` means issues 12 to 15 are missing (12, 13, 14, 15)
 * ``|`` is used as a subfield separator: ``abs. 2018, 12 ; 2019, 15 | suppl. HS 2001``
 * ``…`` is used to mean a series is still going on: ``suppl. HS 2001, 1–…`` means special issues have been regularly published since 2001.


Sample file
--------------

Here are the first 10 lines from the `KBART file describing OpenEdition Open Access Freemium Journals <https://bacon.abes.fr/package2kbart/OPENEDITION_GLOBAL_JOURNALS-OPENACCESS-FREEMIUM_2020-03-09.txt>`_.
It does include the 26th non-standard ``bestppn`` column from BACON.

.. code-block:: tsv

   publication_title	print_identifier	online_identifier	date_first_issue_online	num_first_vol_online	num_first_issue_online	date_last_issue_online	num_last_vol_onlinenum_last_issue_online	title_url	first_author	title_id	embargo_info	coverage_depth	notes	publisher_name	publication_type	date_monograph_published_print	date_monograph_published_online	monograph_volume	monograph_edition	first_editor	parent_publication_title_id	preceding_publication_title_id	access_type	bestppn
   ABE Journal		2275-6639	2012	1					http://journals.openedition.org/abe		abe		fulltext	Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	InVisu	serial								F	187652759
   Afrique : Archéologie et Arts	1634-3123	2431-2045	2004	3					http://journals.openedition.org/aaa		aaa		fulltext	Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	CNRS - UMR 7041 (Archéologie et Sciences de l'Antiquité - ArScAn)	serial								F	190738103
   Afriques		2108-6796	2010	1					http://journals.openedition.org/afriques		afriques		fulltext	Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	Institut des mondes africains (IMAF)	serial					F144221322
   Aitia. Regards sur la culture hellénistique au XXIe siècle		1775-4275	2011	1					http://journals.openedition.org/aitia		aitia		fulltext	Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	ENS Éditions	serial				F15515737X
   Alsic		1286-4986	1998	1	1				http://journals.openedition.org/alsic		alsic		fulltext	Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	Adalsic	serial								F	040654435
   América	0982-9237	2427-9048	2011	40					http://journals.openedition.org/america		america		fulltext	Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	Presses Sorbonne Nouvelle	serial								F187771863
   Amerika		2107-0806	2010	1					http://journals.openedition.org/amerika		amerika		fulltext	Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	LIRA-Université de Rennes 2	serial								F	142582050
   Amérique latine histoire et mémoire	1628-6731	1777-5175	2000	1					http://journals.openedition.org/alhim		alhim		fulltext	Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	Université Paris VIII	serial						F111735939
   Amnis		1764-7193	2001	1					http://journals.openedition.org/amnis		amnis		fulltext	suppl. H.S. 1, 2004 ; H.S. 2, 2011 ; Journées d'études, 2013 ; numéro spécial 2015 ; numéro spécial 2018 | Full access to the HTML version of the content. Access to PDF and Epub reserved to subscribing institutions.	TELEMME - UMR 6570	serial								F	090141377
