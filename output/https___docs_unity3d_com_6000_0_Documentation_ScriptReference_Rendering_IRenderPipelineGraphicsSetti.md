* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineGraphicsSettings.html

# IRenderPipelineGraphicsSettings
interface in UnityEngine.Rendering
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
Classes implementing this interface are stored in [RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html). Use them to store project default data.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.ComponentModel;
using UnityEngine;
using UnityEngine.Rendering;  
  
[
    Serializable,               // required
    Categorization.CategoryInfo("Dummy",1), Categorization.ElementInfo("A",10), // optional: sort out in the Graphics[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html) tab
    SupportedOnRenderPipeline   // optional: which SRP support it
]
public class DummyA : IRenderPipelineGraphicsSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineGraphicsSettings.html)
{
    enum Version
    {
        Initial,  
  
        Count,
        Last = Count - 1
    }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)] Version m_Version = Version.Last;
    int IRenderPipelineGraphicsSettings.version[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineGraphicsSettings-version.html) => (int)m_Version;
    bool IRenderPipelineGraphicsSettings.isAvailableInPlayerBuild[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineGraphicsSettings-isAvailableInPlayerBuild.html) => false;  
  
    // data project wise
    public int myInt = 33;
}

```

### Properties
Property | Description  
---|---  
[isAvailableInPlayerBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineGraphicsSettings-isAvailableInPlayerBuild.html) | If the setting is available in player build.  
[version](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineGraphicsSettings-version.html) | The current version of this settings.  
### Public Methods
Method | Description  
---|---  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineGraphicsSettings.Reset.html) | Optional method to perform custom reset logic.  
* * *
