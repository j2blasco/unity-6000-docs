* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.DiscreteEvaluationAttribute-ctor.html

# DiscreteEvaluationAttribute Constructor
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
public DiscreteEvaluationAttribute(); 
### Description
Use this attribute to indicate that a property will be evaluated as a discrete value during animation playback.
When a property is assigned the DiscreteEvaluation attribute, it is evaluated as a constant value during animation playback. This means that the property's value is neither interpolated between keys nor blended between clips. This affects the evaluation of related AnimationCurves and disables editing the Tangent mode in the Animation window: the [TangentMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationUtility.TangentMode.html) is set to Constant.  
  
Note: The DiscreteEvaluation attribute only supports positive integer values. If an Animation clip is created with a property that is assigned the DiscreteEvaluation attribute and this attribute is modified or removed, the Animation clip cannot be reused.
* * *
