* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-create.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Getting started with Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-getting-started.html)
  * [Android keystores](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore.html)
  * Create a new keystore


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-manager.html)
Keystore Manager window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html)
Add keys to a keystore
# Create a new keystore
This page explains how to use the Keystore Manager window to create a new keystore. 
This is relevant if you want to publish your application, because you must provide a key from a keystore when you sign the application.
To create a new keystore:
  1. Open the [Keystore Manager window](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-manager.html).
  2. In the top-left of the window, select **Keystore** > **Create New**.
  3. Select **Anywhere** and save the keystore file in your Project folder, or select **In Dedicated Location** and save the keystore to a different directory on your computer. For more information, see [Choose the keystore location](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-create.html#choose-the-keystore-location).
  4. Enter a password for the keystore in the **Password** field and re-enter the password in the **Confirm password** field.
  5. A keystore must contain at least one key so to finish creating a keystore, add a key. To do this, see [Add keys to a keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html).


## Choose the keystore location
You can create a new keystore anywhere on your computer, however there are two special locations: the Project folder and what is called the keystores dedicated location. If you place a keystore in either of these places, Unity saves a relative path to the keystore. Otherwise Unity saves an absolute path to the keystore. Under the **Keystore** > **Create New** menu option, there are two options: 
  * **Anywhere** opens the file explorer at the root of your project folder. This is the default place that Unity stores keystores.
  * **In Dedicated Location** opens the file explorer in a custom location. By default, this path points to `$HOME/` on MacOS and to `%USER_HOME%\` on Windows. To change the dedicated location for your computer, go to **Edit** > **Preferences** (macOS: **Unity > Settings**) and then navigate to **External Tools** > **Android** > **Keystores Dedicated Location**. Select **Browse** to choose a location or enter a path in the text box.


If you store a keystore in a dedicated location, Unity saves a relative path from the dedicated location to the keystore. This means different computers can specify a different dedicated location and store the keystore in a different place.
**Note** : If you save the new keystore outside of your Project folder or a shared directory, collaborators on your project might not have access to it. 
## Additional resources
  * [Keystore Manager window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-manager.html)
  * [Add keys to a keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-manager.html)
Keystore Manager window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html)
Add keys to a keystore
