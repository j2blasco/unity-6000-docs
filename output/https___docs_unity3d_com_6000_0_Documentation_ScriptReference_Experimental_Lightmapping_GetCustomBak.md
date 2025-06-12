* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.GetCustomBakeResultsNoCopy.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Lightmapping.html).GetCustomBakeResultsNoCopy
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
public static ReadOnlySpan<Vector4> GetCustomBakeResultsNoCopy(); 
### Returns
**ReadOnlySpan <Vector4>** The unnormalized amount of sky visibility for the input points (in xyz). The w component is the fraction of rays that strike backfaces. 
### Description
Retrieve the custom bake results.
The custom bake calculates the amount of sky visible from the input sample points. The value is computed by shooting rays on the upper hemisphere above each point and the result is the fraction of samples that reach the sky in a direct line from each position (accounting for transparency). Each ray is offset by the value specified in the w component of the input. The result value is a single floating point number and is stored in (xyz) and will be unnormalized. The value can be normalized by dividing with the number of samples used for the custom bake. The w component of the result represent the fraction of samples that strike a backface and can be used to detect samples that lie inside geometry (i.e. they will have a high w value). The data can be used in a custom shader to account for sky visibility on objects that are difficult to bake such as trees and foliage. This way points that lie within the crown of a tree for example will become darker since fewer rays will escape to the sky.
* * *
