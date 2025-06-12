* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.GetPlatformTextureSettings.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).GetPlatformTextureSettings
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html "Go to TextureImporter Component in the Manual")
## Declaration
public bool GetPlatformTextureSettings(string platform, out int maxTextureSize, out [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) textureFormat, out int compressionQuality, out bool etc1AlphaSplitEnabled); 
### Parameters
Parameter | Description  
---|---  
platform | The platform for which settings are required (see options below).  
maxTextureSize | Maximum texture width/height in pixels.  
textureFormat | Format of the texture for the given platform.  
compressionQuality | Value from 0..100, equivalent to the standard JPEG quality setting.  
etc1AlphaSplitEnabled | Status of the ETC1 and alpha split flag.  
### Returns
**bool** True if the platform override was found, false if no override was found. 
### Description
Gets platform specific texture settings.
The values for the chosen platform are returned in the `out` parameters. The options for the `platform` string are as follows: 
  * Standalone
  * Web
  * iPhone
  * Android
  * Windows Store Apps
  * tvOS


```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine.UI;
using System.Collections;  
  
public class DisplayInfo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DisplayInfo.html) : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("PlatformSettings/GetSettingsForAndroid")]
    static void GetAndroidSettings()
    {
        string  platformString = "Android[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html)";
        int     platformMaxTextureSize = 0;
        TextureImporterFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) platformTextureFmt;
        int     platformCompressionQuality = 0;
        bool    platformAllowsAlphaSplit = false;  
  
        TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html) ti = (TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html))TextureImporter.GetAtPath("Assets/characters.png");
        if (ti.GetPlatformTextureSettings(platformString, out platformMaxTextureSize, out platformTextureFmt, out platformCompressionQuality, out platformAllowsAlphaSplit))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Found some overrides for platform: " + platformString);
        }
    }
}

```

* * *
## Declaration
public bool GetPlatformTextureSettings(string platform, out int maxTextureSize, out [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) textureFormat, out int compressionQuality); 
### Parameters
Parameter | Description  
---|---  
platform | The platform whose settings are required (see below).  
maxTextureSize | Maximum texture width/height in pixels.  
textureFormat | Format of the texture.  
compressionQuality | Value from 0..100, equivalent to the standard JPEG quality setting.  
### Returns
**bool** True if the platform override was found, false if no override was found. 
### Description
Gets platform specific texture settings.
The values for the chosen platform are returned in the `out` parameters. The options for the `platform` string are as follows: 
  * Standalone
  * Web
  * iPhone
  * Android
  * Windows Store Apps
  * tvOS


* * *
## Declaration
public bool GetPlatformTextureSettings(string platform, out int maxTextureSize, out [TextureImporterFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html) textureFormat); 
### Parameters
Parameter | Description  
---|---  
platform | The platform whose settings are required (see below).  
maxTextureSize | Maximum texture width/height in pixels.  
textureFormat | Format of the texture.  
### Returns
**bool** True if the platform override was found, false if no override was found. 
### Description
Gets platform specific texture settings.
The values for the chosen platform are returned in the `out` parameters. The options for the `platform` string are as follows: 
  * Standalone
  * Web
  * iPhone
  * Android
  * Windows Store Apps
  * tvOS


* * *
## Declaration
public [TextureImporterPlatformSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings.html) GetPlatformTextureSettings(string platform); 
### Parameters
Parameter | Description  
---|---  
platform | The platform whose settings are required (see below).  
### Returns
**TextureImporterPlatformSettings** A [TextureImporterPlatformSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterPlatformSettings.html) structure containing the platform parameters. 
### Description
Gets platform specific texture settings.
The values for the chosen platform are returned in the `out` parameters. The options for the `platform` string are as follows: 
  * Standalone
  * Web
  * iPhone
  * Android
  * Windows Store Apps
  * tvOS


* * *
