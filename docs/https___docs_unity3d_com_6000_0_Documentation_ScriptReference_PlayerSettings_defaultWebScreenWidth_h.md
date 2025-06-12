* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-defaultWebScreenWidth.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).defaultWebScreenWidth
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
defaultWebScreenWidth; 
### Description
Default horizontal dimension of web player window.
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/PlayerSettingsCustomSettings.png)   
_Custom player settings._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

// Simple Script that saves and loads custom
// Stand-alone/Web player screen settings among
// Unity Projects  
  
class CustomSettings : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{  
  
    string compName = "";
    string prodName = "";
    int screenWidth = 640;
    int screenHeight = 480;
    int webScreenWidth = 640;
    int webScreenHeight = 480;
    bool fullScreen = false;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Custom Settings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditor.Settings.html)")]
        static void Init()
    {
        var window = GetWindow<CustomSettings>();
        window.Show();
    }  
  
    void OnGUI()
    {
        compName = EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)("Company Name:", compName);
        prodName = EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)("Product Name:", prodName);
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        screenWidth = EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)("Width:", screenWidth);
        screenHeight = EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)("Web Height:", screenHeight);
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();
        EditorGUILayout.Space[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Space.html)();
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        webScreenWidth = EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)("Web Width:", webScreenWidth);
        webScreenHeight = EditorGUILayout.IntField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntField.html)("Web Height:", webScreenHeight);
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();
        fullScreen = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("Full Screen[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen.html):", fullScreen);
        EditorGUILayout.BeginHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.BeginHorizontal.html)();
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Save Values"))
            SaveSettings();
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Load Values"))
            LoadSettings();
        EditorGUILayout.EndHorizontal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.EndHorizontal.html)();
    }  
  
    void SaveSettings()
    {
        PlayerSettings.companyName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-companyName.html) = compName;
        PlayerSettings.productName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-productName.html) = prodName;
        PlayerSettings.defaultScreenWidth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-defaultScreenWidth.html) = screenWidth;
        PlayerSettings.defaultScreenHeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-defaultScreenHeight.html) = screenHeight;
        PlayerSettings.defaultWebScreenWidth[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-defaultWebScreenWidth.html) = webScreenWidth;
        PlayerSettings.defaultWebScreenHeight[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-defaultWebScreenHeight.html) = webScreenHeight;
        PlayerSettings.defaultIsFullScreen = fullScreen;  
  
        EditorPrefs.SetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetString.html)("CompName", compName);
        EditorPrefs.SetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetString.html)("ProdName", prodName);
        EditorPrefs.SetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetInt.html)("ScreenWidth", screenWidth);
        EditorPrefs.SetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetInt.html)("ScreenHeight", screenHeight);
        EditorPrefs.SetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetInt.html)("WebScreenWidth", webScreenWidth);
        EditorPrefs.SetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.SetInt.html)("WebScreenHeight", webScreenHeight);
    }
    void LoadSettings()
    {
        compName = EditorPrefs.GetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetString.html)("CompName", "");
        prodName = EditorPrefs.GetString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetString.html)("ProdName", "");
        screenWidth = EditorPrefs.GetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetInt.html)("ScreenWidth", 640);
        screenHeight = EditorPrefs.GetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetInt.html)("ScreenHeight", 480);
        webScreenWidth = EditorPrefs.GetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetInt.html)("WebScreenWidth", 640);
        webScreenHeight = EditorPrefs.GetInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorPrefs.GetInt.html)("WebScreenHeight", 480);
    }
}
```

* * *
