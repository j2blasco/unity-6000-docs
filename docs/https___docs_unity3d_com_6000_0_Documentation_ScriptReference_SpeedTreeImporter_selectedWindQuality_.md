* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-selectedWindQuality.html

#  [SpeedTreeImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.html).selectedWindQuality
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
selectedWindQuality; 
### Description
Gets and sets an integer corresponding to the SpeedTreeWind enum values. The value is clamped by [SpeedTreeImporter.bestWindQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-bestWindQuality.html) internally.
The possible wind quality values are as follows:  
  
`0` - Off  
`1` - Fastest  
`2` - Fast  
`3` - Better  
`4` - Best  
`5` - Palm (only available on palm-like trees)  
  
The SpeedTree Modeler determines the [SpeedTreeImporter.bestWindQuality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-bestWindQuality.html) value, which is then used to limit the available `selectedWindQuality` values. You can lower the wind quality of a SpeedTree model in the Unity Editor based on the application's needs, but you can't improve the wind quality without the SpeedTree Modeler, which generates the necessary wind data in the SpeedTree model file during the export process.   
  
To change this setting for a specific LOD, see [SpeedTreeImporter.windQualities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-windQualities.html) and [SpeedTreeImporter.enableSettingOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-enableSettingOverride.html).
* * *
