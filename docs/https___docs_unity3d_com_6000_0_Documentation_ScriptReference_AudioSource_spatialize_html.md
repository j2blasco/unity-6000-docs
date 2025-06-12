* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-spatialize.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).spatialize
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
spatialize; 
### Description
Enables or disables spatialization.
Custom spatializer effects improve the realism of sound propagation by incorporating the binaural head-related transfer function (HRTF) such that the listener can better sense the directionality of the sound through the filtering of the head and the micro-delays between the ears. Unity supports custom spatialization effects as optional plugins through the native audio plugin system, and in case such plugins are present, will show a "Spatialize" checkbox on the AudioSource that corresponds to this property. If no plugin is present (and selected in the project audio settings), attempts to set this property to true will fail with a warning.
* * *
