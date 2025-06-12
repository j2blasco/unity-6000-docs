* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.SetTextureSettings.html

#  [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).SetTextureSettings
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
public void SetTextureSettings([TextureImporterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html) src); 
### Description
Sets texture importers settings from [TextureImporterSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html) class.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Automatically convert any texture with "SingleChannel"
// in its path into a single channel texture, and set it to use the red color channel.  
  
class SingleChannelPreprocessor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessTexture()
    {
        if (assetPath.Contains("SingleChannel"))
        {
            TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html) textureImporter  = (TextureImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html))assetImporter;
            textureImporter.textureType = TextureImporterType.SingleChannel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterType.SingleChannel.html);
            
            TextureImporterSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html) settings = new TextureImporterSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSettings.html)();
            textureImporter.ReadTextureSettings(settings);
            settings.singleChannelComponent = TextureImporterSingleChannelComponent.Red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterSingleChannelComponent.Red.html);
            textureImporter.SetTextureSettings(settings);
        }
    }
}
```

Additional resources: [TextureImporter.ReadTextureSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.ReadTextureSettings.html).
* * *
