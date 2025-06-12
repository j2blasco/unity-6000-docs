* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.html

# PlayerPrefs
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
`PlayerPrefs` is a class that stores Player preferences between game sessions. It can store string, float and integer values into the user’s platform registry.
Unity stores PlayerPrefs in a local registry, without encryption. Do not use PlayerPrefs data to store sensitive data.  
  
Unity stores `PlayerPrefs` data differently based on which operating system the application runs on. In the file paths given on this page, the ExampleCompanyName and ExampleProductName are the names you set in Unity’s [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html).  
  
  
  
**Standalone player and in-Editor Play mode storage location**  
  
- **MacOS** : `~/Library/Preferences/com.ExampleCompanyName.ExampleProductName.plist`  
  
**Standalone Player storage location**  
  
- **Android** : `/data/data/pkg-name/shared_prefs/pkg-name.v2.playerprefs.xml`.   
  
**Notes** : 
  * Unity uses [SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences) API to access the `PlayerPrefs` data and [SharedPreferences.Editor](https://developer.android.com/reference/android/content/SharedPreferences.Editor) API to modify it.
  * C#, Android Java, and native code can all access the `PlayerPrefs` data.


- **iOS** : Uses the `[NSUserDefaults standardUserDefaults]` API to store PlayerPrefs data.  
  
- **Linux** : `~/.config/unity3d/ExampleCompanyName/ExampleProductName`  
  
- **WebGL** : Unity stores up to 1MB of PlayerPrefs data using the browser's IndexedDB API. For more information, see [IndexedDB](https://developers.google.com/web/ilt/pwa/lab-indexeddb#overview).  
  
- **Windows** : `HKCU\Software\ExampleCompanyName\ExampleProductName`  
  
- **Windows Universal Platform** : `%userprofile%\AppData\Local\Packages\[ProductPackageId]\LocalState\playerprefs.dat`  
  
  
  
**In-Editor Play mode storage location**  
  
- **Windows** : `HKCU\Software\Unity\UnityEditor\ExampleCompanyName\ExampleProductName` key. Note that Windows uses the key names from the application’s PlayerPrefs as a hashed identifier. For example, Unity adds a `DeckBase` string to the hashed key name (for example `h3232628825`) to create `DeckBase_h3232628825`. Unity hashes the names because it: 
  * Allows Unity to store case-sensitive key names.
  * Prevents naming conflicts with data the application stores outside of PlayerPrefs.
  * Ensures that you use the PlayerPrefs API to access and modify the values.


The application ignores the extension.
### Static Methods
Method | Description  
---|---  
[DeleteAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.DeleteAll.html) | Removes all keys and values from the preferences. Use with caution.  
[DeleteKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.DeleteKey.html) | Removes the given key from the PlayerPrefs. If the key does not exist, DeleteKey has no impact.  
[GetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetFloat.html) | Returns the value corresponding to key in the preference file if it exists.  
[GetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetInt.html) | Returns the value corresponding to key in the preference file if it exists.  
[GetString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.GetString.html) | Returns the value corresponding to key in the preference file if it exists.  
[HasKey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.HasKey.html) | Returns true if the given key exists in PlayerPrefs, otherwise returns false.  
[Save](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.Save.html) | Saves all modified preferences.  
[SetFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.SetFloat.html) | Sets the float value of the preference identified by the given key. You can use PlayerPrefs.GetFloat to retrieve this value.  
[SetInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.SetInt.html) | Sets a single integer value for the preference identified by the given key. You can use PlayerPrefs.GetInt to retrieve this value.  
[SetString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerPrefs.SetString.html) | Sets a single string value for the preference identified by the given key. You can use PlayerPrefs.GetString to retrieve this value.   
* * *
