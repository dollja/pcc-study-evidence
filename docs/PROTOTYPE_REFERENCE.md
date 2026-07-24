# Canonical prototype reference

The evidence repository references the prototype repository; it does not duplicate the application source.

- Repository: `dollja/interpretive-drift-protoype`
- Frozen baseline commit: `d6af4b461bd1623fc1021cb1ccc063dbc14498e2`
- Cloud entrypoint: `app.py`
- Reviewer application: `streamlit_app.py`
- Step 1 extractor: `variable_extractor.py`
- Extractor tests: `tests/test_variable_extractor.py`

At the frozen commit, `app.py` re-executes `streamlit_app.py` through `runpy.run_path`, and the reviewer application imports `extract_coordination_critical_variables` from `variable_extractor.py`. This is sufficient to trace proposal statements to the canonical source revision.

A separate application-source upload is unnecessary while this commit remains accessible and corresponds to the reviewed demo. If the active Streamlit deployment contains local, private, or unpushed changes, those changes must first be committed to the prototype repository; the evidence register should then record the new immutable commit SHA rather than storing a second source copy here.
