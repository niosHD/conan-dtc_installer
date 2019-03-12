# BINTRAY_API_KEY has to be defined accordingly
USER=nioshd
CHANNEL=testing
REMOTE=origin

# inspect the recipe to determine the name and version
NAME=$(conan inspect . -a name | sed -e "s/^name: //")
VERSION=$(conan inspect . -a version | sed -e "s/^version: //")

# build the package
conan create . "$NAME/$VERSION@$USER/$CHANNEL" --build=outdated

# add the bintray remote and authenticate
conan remote add "$REMOTE" "https://api.bintray.com/conan/$USER/conan" --insert 0
conan user "$USER" -p "$BINTRAY_API_KEY" -r "$REMOTE"

# upload the built package and recipe
conan upload "$NAME/$VERSION@$USER/$CHANNEL" -r "$REMOTE" --all -c
