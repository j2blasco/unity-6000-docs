* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-windQualities.html

#  [SpeedTreeImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.html).windQualities
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
windQualities; 
### Description
Gets and sets an array of integers of the wind qualities on each LOD. Values will be clamped by [SpeedTreeImporter.bestWindQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-bestWindQuality.html) internally.
The available wind quality values are as follows:  
  
`0` - Off  
`1` - Fastest  
`2` - Fast  
`3` - Better  
`4` - Best  
`5` - Palm (only available on palm-like trees)  
  
Because the higher wind qualities come with an increased performance cost, you may want assign higher quality wind effects to only the SpeedTree assets that are nearest to the player. You can use this feature to improve performance by using lower-quality wind effects on some of your less detailed LOD levels where the models are far enough away from the camera that the lower quality of this effect is not noticeable. The array length that you supply must match the number of LOD levels in your SpeedTree asset, and typically would have true values at the start, and false values at the end. For example, if your SpeedTree asset has three LOD levels, you might pass an array of `[ 4, 3, 2]` to enable the "Best" wind effect on the nearest LOD level, the "Better" on the second LOD level, and "Faster" on the third and most distant LOD level.
* * *
