* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseSlider_1-movableUssClassName.html

#  [BaseSlider<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseSlider_1.html).movableUssClassName
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
movableUssClassName; 
### Description
USS class name on the dragger that indicates it is currently controlled by [NavigationMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.html). When the slider detects move events aligned with the slider's direction, it adjusts the slider's value. If it detects a navigation submit event, it removes the style, causing all navigation events to revert to their default behavior. A second navigation submit event re-applies the style to the dragger and restores the previous customized behavior. 
* * *
