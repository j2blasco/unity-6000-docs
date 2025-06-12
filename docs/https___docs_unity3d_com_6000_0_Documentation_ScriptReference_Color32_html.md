* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html

# Color32
struct in UnityEngine
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
Representation of RGBA colors in 32 bit format.
Each color component is a byte value with a range from 0 to 255.  
  
Components ([r](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-r.html),[g](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-g.html),[b](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-b.html)) define a color in RGB color space. Alpha component ([a](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-a.html)) defines transparency - alpha of 255 is completely opaque, alpha of zero is completely transparent.
### Properties
Property | Description  
---|---  
[a](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-a.html) | Alpha component of the color.  
[b](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-b.html) | Blue component of the color.  
[g](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-g.html) | Green component of the color.  
[r](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-r.html) | Red component of the color.  
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.Index_operator.html) | Access the red (r), green (g), blue (b), and alpha (a) color components using [0], [1], [2], [3] respectively.  
### Constructors
Constructor | Description  
---|---  
[Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-ctor.html) | Constructs a new Color32 with given r, g, b, a components.  
### Public Methods
Method | Description  
---|---  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.ToString.html) | Returns a formatted string for this color.  
### Static Methods
Method | Description  
---|---  
[Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.Lerp.html) | Linearly interpolates between colors a and b by t.  
[LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.LerpUnclamped.html) | Linearly interpolates between colors a and b by t.  
### Operators
Operator | Description  
---|---  
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-operator_Color32.html) | Color32 can be implicitly converted to and from Color.  
[Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32-operator_Color.html) | Color32 can be implicitly converted to and from Color.  
* * *
