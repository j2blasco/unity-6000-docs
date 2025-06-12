* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundPropertyHelper.ResolveUnityBackgroundScaleMode.html

#  [BackgroundPropertyHelper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundPropertyHelper.html).ResolveUnityBackgroundScaleMode
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
public static [ScaleMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScaleMode.html) ResolveUnityBackgroundScaleMode([UIElements.BackgroundPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundPosition.html) backgroundPositionX, [UIElements.BackgroundPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundPosition.html) backgroundPositionY, [UIElements.BackgroundRepeat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundRepeat.html) backgroundRepeat, [UIElements.BackgroundSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BackgroundSize.html) backgroundSize, out bool valid); 
### Parameters
Parameter | Description  
---|---  
backgroundPositionX | The X BackgroundPosition to resolve.  
backgroundPositionY | The Y BackgroundPosition to resolve.  
backgroundRepeat | The BackgroundRepeat to resolve.  
backgroundSize | The BackgroundSize to resolve.  
valid | Indicates whether the background properties resolve to a valid ScaleMode.  
### Returns
**ScaleMode** ScaleMode. 
### Description
Resolves the background properties to a valid ScaleMode. 
* * *
