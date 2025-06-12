* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html

# Color
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
Representation of RGBA colors.
This structure is used throughout Unity to pass colors around. Each color component is a floating point value with a range from 0 to 1.  
  
Components ([r](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-r.html),[g](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-g.html),[b](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-b.html)) define a color in RGB color space. Alpha component ([a](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-a.html)) defines transparency - alpha of one is completely opaque, alpha of zero is completely transparent.
### Static Properties
Property | Description  
---|---  
[black](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-black.html) | Solid black. RGBA is (0, 0, 0, 1).  
[blue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html) | Solid blue. RGBA is (0, 0, 1, 1).  
[clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-clear.html) | Completely transparent. RGBA is (0, 0, 0, 0).  
[cyan](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-cyan.html) | Cyan. RGBA is (0, 1, 1, 1).  
[gray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-gray.html) | Gray. RGBA is (0.5, 0.5, 0.5, 1).  
[green](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html) | Solid green. RGBA is (0, 1, 0, 1).  
[grey](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-grey.html) | English spelling for gray. RGBA is the same (0.5, 0.5, 0.5, 1).  
[magenta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-magenta.html) | Magenta. RGBA is (1, 0, 1, 1).  
[red](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html) | Solid red. RGBA is (1, 0, 0, 1).  
[white](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html) | Solid white. RGBA is (1, 1, 1, 1).  
[yellow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html) | Yellow. RGBA is (1, 0.92, 0.016, 1), but the color is nice to look at!  
### Properties
Property | Description  
---|---  
[a](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-a.html) | Alpha component of the color (0 is transparent, 1 is opaque).  
[b](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-b.html) | Blue component of the color.  
[g](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-g.html) | Green component of the color.  
[gamma](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-gamma.html) | A version of the color that has had the gamma curve applied.  
[grayscale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-grayscale.html) | The grayscale value of the color. (Read Only)  
[linear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-linear.html) | A linear value of an sRGB color.  
[maxColorComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-maxColorComponent.html) | Returns the maximum color component value: Max(r,g,b).  
[r](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-r.html) | Red component of the color.  
[this[int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Index_operator.html) | Access the r, g, b,a components using [0], [1], [2], [3] respectively.  
### Constructors
Constructor | Description  
---|---  
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-ctor.html) | Constructs a new Color with given r,g,b,a components.  
### Public Methods
Method | Description  
---|---  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.ToString.html) | Returns a formatted string of this color.  
### Static Methods
Method | Description  
---|---  
[HSVToRGB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.HSVToRGB.html) | Creates an RGB colour from HSV input.  
[Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Lerp.html) | Linearly interpolates between colors a and b by t.  
[LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.LerpUnclamped.html) | Linearly interpolates between colors a and b by t.  
[RGBToHSV](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.RGBToHSV.html) | Calculates the hue, saturation and value of an RGB input color.  
### Operators
Operator | Description  
---|---  
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-operator_Vector4.html) | Colors can be implicitly converted to and from Vector4.  
[operator -](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-operator_subtract.html) | Subtracts color b from color a. Each component is subtracted separately.  
[operator *](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-operator_multiply.html) | Multiplies two colors together. Each component is multiplied separately.  
[operator /](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-operator_divide.html) | Divides color a by the float b. Each color component is scaled separately.  
[operator +](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-operator_add.html) | Adds two colors together. Each component is added separately.  
[Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-operator_Color.html) | Colors can be implicitly converted to and from Vector4.  
* * *
