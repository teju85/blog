CFG        := config.json
SRC_BRANCH := gh-pages


default:
	@echo "make what? Available targets are:"
	@echo " . commit    - commit all the changes locally."
	@echo " . push      - push the changes to the remote repo."
	@echo " . publish   - generate the pages, commit the changes and then"
	@echo "               push everything to the remote repo."
	@echo " . serve     - start the server to test changes locally"
	@echo " . generate  - generate the pykyll pages"

generate:
	env PYTHONPATH=gen python gen/pykyll.py -cfg $(CFG)

commit:
	@read -p "Enter commit message: " cmtMsg && \
	    $(MAKE) COMMIT_MSG="$$cmtMsg" _commit

push:
	git push origin $(SRC_BRANCH)

publish:
	$(MAKE) commit push

_commit:
	git add -A
	git commit -m "$(COMMIT_MSG)"
	$(MAKE) generate
	git add -A
	git commit -m "$(COMMIT_MSG)"

serve:
	env PYTHONPATH=gen python gen/pykyll.py -serve
