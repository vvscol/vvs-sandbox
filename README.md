# vvs-sandbox
Sandbox for VVS agents end-to-end tests

Sandbox where VVS's Paperclip agents test the development flow end to end (spec, plan, TDD, VERDICT reviews). Run the tests with `PYTHONPATH=src python3 -m unittest discover -s tests -v` (standard library only: the agents' VM has no pip).
