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
	@echo " . build     - build jekyll pages. Assumes that you are inside"
	@echo "               the 'master' branch!"
	@echo " . publish   - publish the built pages as well as original"
	@echo "               changes to remote repo. Assumes that you are"
	@echo "               inside the 'master' branch!"
	@echo " . serve     - start the server to test changes locally. Assumes"
	@echo "               that you are inside the 'master' branch!"
	@echo " . clean     - clean temporary files"

build:
	git checkout $(SRC_BRANCH)
	jekyll build -s $(SRC_DIR) -d $(SITE_DIR)
	git checkout $(DST_BRANCH)
	git rm -qr .
	cp -r $(SITE_DIR) .

publish:
	git add -A
	git commit
	git checkout $(DST_BRANCH)
	git add -A
	git commit
	git push origin $(SRC_BRANCH) $(DST_BRANCH)

serve:
	jekyll serve -s $(SRC_DIR) -d $(SITE_DIR)

clean:
	rm -f .sass-cache $(SITE_DIR)
