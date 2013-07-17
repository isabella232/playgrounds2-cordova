Setup
=====

(This assumes you already have XCode.)

Install initial dependencies:

* `brew install android-sdk`
* `brew install ios-sim`

Setup the Android SDK:

* Run `android`
* Install all the packages under "Tools" and "Android 4.2.2 (API 17)"
* Run `android avd`
* Click over the "Device Definitions tab", select "Nexus One" (or whatever) and click "Create AVD...". Select "Android 4.2.2" for the Target and "ARM" for the CPU. Then click OK.

Install Cordova:

* `sudo npm install -g cordova`

Building
========

Running `fab build` will build both iOS and Android versions. You can use, e.g. `fab build:ios`, to just build one or the other.

Running
=======

Run in the Android emulator:

* `fab android`

(Note: the first one or two times you run the Android emulator it will go through a initial device setup process and may fail to install the project. Just close the emulator and run it again.)

Run in the iOS emulator:

* `fab ios`

(Note: the iOS emulator doesn't work when in a tmux window. You'll have to run it directly from Terminal or iTerm.)
