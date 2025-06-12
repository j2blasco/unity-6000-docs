* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils-virtualCameraPreviewInstantiator.html

#  [CameraEditorUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraEditorUtils.html).virtualCameraPreviewInstantiator
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
virtualCameraPreviewInstantiator; 
### Description
Override this function to pass your own Camera provider to generate previews for virtual cameras.
When set, the Cameras Overlay uses the returned Camera to generate previews for virtual cameras, such as the Cinemachine Camera, which are not represented by a Camera instance. This is useful when a camera GameObject must have additional components.
* * *
