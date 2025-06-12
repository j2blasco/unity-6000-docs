* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPreprocessAudio.html

#  [AssetPostprocessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html).OnPreprocessAudio()
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
Add this function to a subclass to get a notification just before an audio clip is being imported.
This lets you control the import settings trough code.
```
using System.Collections;
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class MyAudioPostprocessor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    void OnPreprocessAudio()
    {
        if (assetPath.Contains("mono"))
        {
            AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html) audioImporter = (AudioImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioImporter.html))assetImporter;
            audioImporter.forceToMono = true;
        }
    }
}

```

* * *
