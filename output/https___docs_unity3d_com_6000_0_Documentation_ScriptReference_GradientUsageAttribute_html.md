* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute.html

# GradientUsageAttribute
class in UnityEngine
/
Inherits from:[PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html)
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
Controls how the [Gradient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) inspector editor treats the color values.
Use this attribute on a Gradient public script variable. You can control the [colorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute-colorSpace.html) and [hdr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute-hdr.html) flags.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Inspector editor for this gradient
    // allows to setup regular low dynamic range
    // colors.
    public Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) defaultGradient;  
  
    // Inspector editor for this gradient allows
    // to setup HDR colors.
    [GradientUsage(true)]
    public Gradient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gradient.html) hdrGradient;
}

```

### Properties
Property | Description  
---|---  
[colorSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute-colorSpace.html) | The color space the Gradient uses.  
[hdr](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute-hdr.html) | If set to true the Gradient uses HDR colors.  
### Constructors
Constructor | Description  
---|---  
[GradientUsageAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GradientUsageAttribute-ctor.html) | Attribute for gradient fields. Used to configure the GUI for the Gradient Editor.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
