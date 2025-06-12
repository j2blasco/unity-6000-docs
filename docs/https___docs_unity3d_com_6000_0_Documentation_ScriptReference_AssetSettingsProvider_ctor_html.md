* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider-ctor.html

# AssetSettingsProvider Constructor
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
## Declaration
public AssetSettingsProvider(string settingsWindowPath, Func<Editor> editorCreator, IEnumerable<string> keywords); 
## Declaration
public AssetSettingsProvider(string settingsWindowPath, Func<Object> settingsGetter); 
### Parameters
Parameter | Description  
---|---  
settingsWindowPath | Path of the settings in the Settings window. Uses "/" as separator. The last token becomes the settings label if none is provided.  
editorCreator | Functor creating an [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) able to modify the settings.  
keywords | List of keywords to compare against what the user is searching for. When the user enters values in the search box on the Settings window, [SettingsProvider.HasSearchInterest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.HasSearchInterest.html) tries to match those keywords to this list.  
settingsGetter | Functor creating or getting a settings object.  
### Description
Creates a new AssetSettingsProvider so you can wrap legacy settings (that is, settings that previously appeared in the Inspector).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
// Create a new type of Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html).
class MyCustomSettings : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public const string k_MyCustomSettingsPath = "Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/MyCustomSettings.asset";  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private int m_Number;  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private string m_SomeString;  
  
    internal static SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) GetSettings()
    {
        var settings = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<MyCustomSettings>(k_MyCustomSettingsPath);
        if (settings == null)
        {
            settings = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MyCustomSettings>();
            settings.m_Number = 42;
            settings.m_SomeString = "The answer to the universe";
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(settings, k_MyCustomSettingsPath);
        }  
  
        return new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(settings);
    }
}  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyCustomSettings))]
class MyCustomSettingsEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    // Nothing to do. This uses the Generic Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) to display MyCustomSettings properties
}  
  
class AssetSettingsProviderRegister
{
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateFromFilePath()
    {
        // Create an AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) from a file path:
        var provider = AssetSettingsProvider.CreateProviderFromAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromAssetPath.html)("Project/AssetSettings/FromFile", MyCustomSettings.k_MyCustomSettingsPath);  
  
        // Register keywords from the properties of MyCustomSettings
        provider.keywords = SettingsProvider.GetSearchKeywordsFromSerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(AssetDatabase.LoadAllAssetsAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetsAtPath.html)(MyCustomSettings.k_MyCustomSettingsPath)));
        return provider;
    }  
  
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateFromSettingsObject()
    {
        // Create an AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) from a settings object (UnityEngine.Object):
        var settingsObj = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath);
        var provider = AssetSettingsProvider.CreateProviderFromObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromObject.html)("Project/AssetSettings/FromObject", settingsObj);  
  
        // Register keywords from the properties of MyCustomSettings
        provider.keywords = SettingsProvider.GetSearchKeywordsFromSerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(settingsObj));
        return provider;
    }  
  
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateFromSettingsFromFunctor()
    {
        // Create an AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) from a functor that must return a UnityEngine.Object:
        var provider = new AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html)("Project/AssetSettings/FromFunctor", () => Editor.CreateEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.CreateEditor.html)(AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath)));  
  
        // Register keywords from the properties of MyCustomSettings
        provider.keywords = SettingsProvider.GetSearchKeywordsFromSerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(AssetDatabase.LoadAllAssetsAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetsAtPath.html)(MyCustomSettings.k_MyCustomSettingsPath)));
        return provider;
    }
}

```

* * *
