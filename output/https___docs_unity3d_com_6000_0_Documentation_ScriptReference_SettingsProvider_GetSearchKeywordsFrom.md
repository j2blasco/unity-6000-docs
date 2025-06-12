* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromSerializedObject.html

#  [SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html).GetSearchKeywordsFromSerializedObject
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
public static IEnumerable<string> GetSearchKeywordsFromSerializedObject([SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject); 
### Parameters
Parameter | Description  
---|---  
serializedObject | Object to extract properties from.  
### Returns
**IEnumerable <string>** Returns the list of keywords. 
### Description
Extract search keywords from from the serialized properties of a [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Create a new type of Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html).
class MyCustomSettings : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public const string k_MyCustomSettingsPath = "Assets/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)/MyCustomSettings.asset";  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private int m_Number;  
  
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    private string m_SomeString;  
  
    internal static MyCustomSettings GetOrCreateSettings()
    {
        var settings = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<MyCustomSettings>(k_MyCustomSettingsPath);
        if (settings == null)
        {
            settings = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MyCustomSettings>();
            settings.m_Number = 42;
            settings.m_SomeString = "The answer to the universe";
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(settings, k_MyCustomSettingsPath);
            AssetDatabase.SaveAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html)();
        }
        return settings;
    }  
  
    internal static SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) GetSerializedSettings()
    {
        return new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(GetOrCreateSettings());
    }
}  
  
class AssetSettingsProviderRegister
{
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateFromFilePath()
    {
        // Create an AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) from a file path:
        var provider = AssetSettingsProvider.CreateProviderFromAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromAssetPath.html)("Project/AssetSettings/FromFile", MyCustomSettings.k_MyCustomSettingsPath);  
  
        // Register keywords from the properties of the serialized object at a specific path
        provider.keywords = SettingsProvider.GetSearchKeywordsFromPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromPath.html)(MyCustomSettings.k_MyCustomSettingsPath);
        return provider;
    }  
  
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateFromSettingsObject()
    {
        // Create an AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) from a settings object (UnityEngine.Object):
        var settingsObj = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath);
        var provider = AssetSettingsProvider.CreateProviderFromObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.CreateProviderFromObject.html)("Project/AssetSettings/FromObject", settingsObj);  
  
        // Register keywords from the properties of settingsObj
        provider.keywords = SettingsProvider.GetSearchKeywordsFromSerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromSerializedObject.html)(new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(settingsObj));
        return provider;
    }  
  
    class Styles
    {
        public static GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) number = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("My Number");
        public static GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) someString = new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Some string");
    }  
  
    [SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html)]
    public static SettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html) CreateFromSettingsFromFunctor()
    {
        // Create an AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html) from a functor that must return a UnityEngine.Object:
        var provider = new AssetSettingsProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetSettingsProvider.html)("Project/AssetSettings/FromFunctor", () => UnityEditor.Editor.CreateEditor(AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(MyCustomSettings.k_MyCustomSettingsPath)));  
  
        // Register keywords from the static GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) in Styles class
        provider.keywords = SettingsProvider.GetSearchKeywordsFromGUIContentProperties[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.GetSearchKeywordsFromGUIContentProperties.html)<Styles>();
        return provider;
    }
}

```

* * *
