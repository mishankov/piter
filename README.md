```bash
# new env
piter env dev
piter env test

# install, remove and reinstall env 
piter env dev --install
piter env dev -i

piter env dev --remove
piter env dev -r

piter env dev --reinstall
piter env dev -ri

# activate env
piter env dev --activate
piter env dev -a

# deactivate env
piter env --deactivate
piter env -d

# update dependency
piter env dev --update dep_name
piter env dev -u dep_name

# update all dependencies
piter env dev --update
piter env dev -u

# add dependency
piter install dep_name

#add dependencies for env
piter install --environment test dep_name
piter install -e test dep_name

# update dependencies
piter update dep_name
piter update # all dependencies

# update dependencies in env
piter update --environment test dep_name
piter update -e test dep_name # same as piter env dev -u dep_name
piter update -e test # all dependencies. same as piter env test -u

# run scripts in env
piter run --environment test test
piter run -e dev build

# run global scripts
piter run some_script
piter run some_script --no-env # run script without activated environment

```