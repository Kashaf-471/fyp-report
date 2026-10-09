# Current report visuals

Chapter 4 now uses the simplified HTML screen designs and their rendered assets. All source files belong to Kashaf. main.tex and FastFyp.cls remain frozen.

## GUI

Editable pages: stitch_zeest_clinical_support_system/stitch_zeest_clinical_support_system/. Keep styles.css, preview.js and assets/ with the pages. SCREENS.md maps pages to users/use cases. Screens are static design previews; they do not authenticate, record, analyse, approve or evaluate.

Report assets: Report template/Figures/kashaf_G01_signup.png through kashaf_G16_evaluation.png, including separate tab and dialog views. Captions and the coverage tables identify Physician or Research team and UC01?UC22. The medical background is generated decorative artwork, not a clinical screenshot.

## Navigation

kashaf_navigation_preview.html is the editable primary-user thumbnail board. kashaf_D02_primary_navigation.png is its report image. kashaf_D02_doctor_navigation.puml preserves the same semantic flow as a coloured activity diagram. kashaf_research_navigation.puml supplies the research navigation image. Clinical Review branches to modification, approval or rejection; logging out returns to Login.

## Database

kashaf_schema.json is the logical schema source: eighteen entities, ninety-one attributes and twenty-one relationships. Names and fields match the current Chapter 4 dictionary. Proposal/ProposalRevision store the clinical draft and its saved revisions; these are design entity names, not references to the project-proposal document.

The Chen-style report views use Graphviz DOT because PlantUML does not reproduce the attached rectangle/diamond/oval style directly. kashaf_D03_relationships_clinical.dot, review.dot, sources.dot and evaluation.dot split the relationship diagram into readable domain views. kashaf_D03_attributes_1.dot through _6.dot supply attribute views. Primary keys are underlined; FK marks foreign keys. The complete overview DOT and kashaf_D03_hybrid_memory_er.puml retain alternative whole-model sources.

Dictionary keys must be interpreted with composite foreign-key pairing and the validation rules following the tables. Ownership is derived through Patient.physician_id. Revision links retain exact source content; approval records the reviewed revision and matching actor. Semantic memory has exactly one input-revision or approved-decision source. Evaluation rows describe intended storage rather than existing results.

Older three-screen figures and old rendered ER/navigation images are superseded report drafts and remain preserved. The current chapter includes only the new mapped figures.


## Current navigation/ERD correction

The screen-thumbnail navigation is retained, and kashaf_D02_doctor_navigation.puml now supplies an additional coloured Physician/Zeest swimlane included in the report. Both views are present.

The report ERD now follows the supplied grouped conceptual examples: one complete model combines all eighteen entity rectangles, twenty-one named relationship diamonds and ninety-one attribute ovals. Four enlarged regions use the same model. The former separated relationship and attribute sheets are historical drafts and are no longer included. Current editable sources are kashaf_D03_conceptual_combined.svg and kashaf_D03_combined_clinical.svg, _drafts.svg, _review.svg and _evaluation.svg. Native SVG layout was used for predictable grouping and spacing. Corresponding vector PDFs are inserted in the report so labels stay sharp when zoomed; PNGs remain for quick previews. Dictionary entities and fields are unchanged.
