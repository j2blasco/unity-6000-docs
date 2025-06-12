* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter-forceToMono.html

#  [AudioImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html).forceToMono
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
forceToMono; 
### Description
Force audioclips to mono sound type, so all audio plays through a single channel.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessAudio()
    {
        AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) audioImporter = assetImporter as AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html);
        if (assetPath.Contains("mono"))
        {
            audioImporter = assetImporter as AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html);
            audioImporter.forceToMono = true;
        }
    }
}

```

* * *
