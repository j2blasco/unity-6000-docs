* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableSubsurface.html

#  [SpeedTreeImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.html).enableSubsurface
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SpeedTreeImporter.html "Go to SpeedTreeImporter Component in the Manual")
enableSubsurface; 
### Description
Gets and sets an array of booleans to enable the subsurface scattering effect for each LOD (affects only SpeedTree v8 assets).
This setting controls the light scattered out the back side of leaves and other two-sided SpeedTree materials. Because the subsurface scattering effect comes with an increased performance cost, you may want to enable it only on the SpeedTree assets that are nearest to the player. You can improve performance by disabling the subsurface scattering effect on less detailed LOD levels where the models are far enough away from the camera that the absence of this effect is not noticeable. The array length that you supply must match the number of LOD levels in your SpeedTree asset and typically has true values at the start and false values at the end. For example, if your SpeedTree asset has three LOD levels, you might pass an array of `[ true, true, false ]` to enable the subsurface scattering effect on the first two LOD levels, but disable it on the third.
* * *
