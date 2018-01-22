# where to temporarily build the static pages
SITE_DIR   = _site
# source branch, where to build the static pages
SRC_BRANCH = master
# source directory which contains jekyll files
SRC_DIR    = src
# branch used to publish the static pages
DST_BRANCH = gh-pages


default:
	@echo "make what? Available targets are:"
	@echo " . publish   - publish the built pages as well as original"
	@echo "               changes to remote repo. Assumes that you are"
	@echo "               inside the 'master' branch!"
	@echo " . serve     - start the server to test changes locally. Assumes"
	@echo "               that you are inside the 'master' branch!"

publish:
	jekyll build -s $(SRC_DIR) -d $(SITE_DIR)
	git add -A
	EDITOR=vi git commit
	git checkout $(DST_BRANCH)
	git rm -qr `ls -I $(SITE_DIR)`
	cp -r $(SITE_DIR)/* .
	git add -A
	EDITOR=vi git commit
	git checkout $(SRC_BRANCH)
	git push origin $(SRC_BRANCH) $(DST_BRANCH)

serve:
	jekyll serve -s $(SRC_DIR) -d $(SITE_DIR)
