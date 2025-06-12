* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-load.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Getting started with Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-getting-started.html)
  * [Android keystores](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore.html)
  * Load a keystore


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html)
Add keys to a keystore
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
Developing for Android
# Load a keystore
This page explains how to load an existing keystore and select a key from it to use as the project key.
This is relevant if you want to publish your application, because you must provide a key from a keystore when you sign the application.
To load an existing keystore:
  1. Open [Android Publishing Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing).
  2. Under the **Project Keystore** heading, enable **Custom Keystore**.
  3. Click the drop-down below **Custom Keystore**.
  4. Select **Browse** to load a keystore from your file system, or select a keystore from below the partition in the UI. The keystores below the partition are those stored in the keystores dedicated location. For more information, see [Choose the keystore location](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-create.html#choose-the-keystore-location).
  5. Enter the password for the keystore in the **Password** property field. If the password is correct, Unity loads the keystore.


## Select a project key
After you load a keystore into your project, select a key from the keystore to use as the project key. To do this:
  1. Open [Android Publishing Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing).
  2. Under the **Project Key** heading, set **Alias** to the key you want to use.
  3. In the **Password** property field, enter the password for the key.


## Additional resources
  * [Keystore Manager window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-manager.html)
  * [Add keys to a keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html)
  * [useCustomKeystore API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-useCustomKeystore.html)
  * [keystoreName API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keystoreName.html)
  * [keystorePass API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keystorePass.html)
  * [keyaliasName API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keyaliasName.html)
  * [keyaliasPass API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-keyaliasPass.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html)
Add keys to a keystore
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
Developing for Android
