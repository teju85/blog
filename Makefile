# where to temporarily build the static pages
SITE_DIR   = _site
# source branch, where to build the static pages
SRC_BRANCH = master
# source directory which contains jekyll files
SRC_DIR    = src
# branch used to publish the static pages
DST_BRANCH = gh-pages
CFG        = config.json


default:
	@echo "make what? Available targets are:"
	@echo " . commit    - commit all the changes locally. Assumes that you"
	@echo "               are inside the '$(SRC_BRANCH)' branch!"
	@echo " . push      - push the changes to remote repo."
	@echo " . publish   - commit and then push to remote repo"
	@echo " . serve     - start the server to test changes locally. Assumes"
	@echo "               that you are inside the '$(SRC_BRANCH)' branch!"
	@echo " . init      - setup all required packages"
	@echo " . generate  - generate the pykyll pages"

publish:
	$(MAKE) commit push

push:
	git push origin $(SRC_BRANCH) $(DST_BRANCH)

commit:
	@read -p "Enter commit message: " cmtMsg && \
	    $(MAKE) COMMIT_MSG="$$cmtMsg" _commit

_commit:
	jekyll build -s $(SRC_DIR) -d $(SITE_DIR)
	git add -A
	git commit -m "$(COMMIT_MSG)"
	git checkout $(DST_BRANCH)
	cp -r $(SITE_DIR)/* .
	git add -A
	git commit -m "$(COMMIT_MSG)"
	git checkout $(SRC_BRANCH)

serve:
	cd $(SRC_DIR) && bundle exec jekyll serve -d $(SITE_DIR)

init:
	cd $(SRC_DIR) && bundle install --full-index

generate:
	env PYTHONPATH=gen python gen/pykyll.py -cfg $(CFG)
