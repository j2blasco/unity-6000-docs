* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter-scaleFactor.html

#  [SpeedTreeImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpeedTreeImporter.html).scaleFactor
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
scaleFactor; 
### Description
How much to scale the tree model compared to what is in the imported SpeedTree model file.
In the Unity Editor, the SpeedTreeImporter provides a dropdown with the following unit conversion options, which drive the `scaleFactor` value:  
  
`0` - LeaveAsIs : 1.0   
`1` - FeetToMeters : 0.3048   
`2` - CentimetersToMeters : 0.01   
`3` - InchesToMeters : 0.0254   
`4` - CustomConversion : user specified value  
  
  
By default, the SpeedTree Modeler exports units in feet. Because Unity's default units are meters, the default value for `scaleFactor` is set to `0.3048`. 
* * *
