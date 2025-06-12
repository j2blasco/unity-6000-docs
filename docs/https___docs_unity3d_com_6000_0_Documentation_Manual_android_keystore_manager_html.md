* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-manager.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Getting started with Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-getting-started.html)
  * [Android keystores](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore.html)
  * Keystore Manager window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore.html)
Android keystores
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-create.html)
Create a new keystore
# Keystore Manager window reference
This page describes the Keystore Manager window interface.
To open the Keystore Manager window, open [Android Publishing Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Publishing) and select **Keystore Manager**.
You can use this interface to:
  * [Create a new keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-create.html)
  * [Add keys to a keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html)
  * [Load an existing keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-load.html)


## Keystore
The properties in this section of the interface relate to the keystore that the Keystore Manager window currently manages.
**Property** | **Description**  
---|---  
**Keystore dropdown** | Specifies which keystore to use in the Keystore Manager window. You can either create a new keystore, or load an existing one. For more information, refer to:
  * [Create a new keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-create.html)
  * [Load an existing keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-load.html)

  
**Password** | The password for the keystore. If you create a new keystore, use this to create a password for the keystore. If you load an existing keystore, use this to enter the password for existing keystore. This property supports ASCII characters only.  
**Confirm Password** | The confirmed password for the new keystore. Set the value of this property to the same as **Password**.  
  
This property only appears if you create a new keystore.  
## Existing Keys
This section of the interface contains a read-only list of keys that the current keystore contains.
## New Key Values
The properties in this section of the interface describe a new key to add to the keystore. For more information, see [Add keys to a keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html).
**Note** : The application doesn’t display the personal information in this section. Instead, the certificate that is part of your application includes it.
**Property** | **Description**  
---|---  
**Alias** | An identifying name for the key.  
**Password** | The password to use for the key. This property supports ASCII characters only.  
**Confirm password** | The confirmed password for the key. Set the value of this property to the same as **Password**.  
**Validity (years)** | The number of years that the key is valid for. This should exceed the amount of time you expect to manage the application for, so that you can use the same key to sign application updates. The default validity is 50 years.  
**First and Last Name** | Your first and last name.  
**Organizational Unit** | The division of your organization that you are part of.  
**Organization** | The organization that manages your application. This is often your company name.  
**City or Locality** | Your personal city or locality.  
**State or Province** | Your personal state or province.  
**Country Code** | Your personal country code.  
## Additional resources
  * [Create a new keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-create.html)
  * [Add keys to a keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-add-keys.html)
  * [Load a keystore](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-load.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore.html)
Android keystores
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-keystore-create.html)
Create a new keystore
