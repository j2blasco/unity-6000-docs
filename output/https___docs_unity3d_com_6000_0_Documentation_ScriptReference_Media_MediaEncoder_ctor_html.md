* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.MediaEncoder-ctor.html

# MediaEncoder Constructor
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
public MediaEncoder(string filePath, [Media.VideoTrackAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackAttributes.html) videoAttrs, AudioTrackAttributes[] audioAttrs); 
## Declaration
public MediaEncoder(string filePath, [Media.VideoTrackEncoderAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes.html) videoAttrs, AudioTrackAttributes[] audioAttrs); 
## Declaration
public MediaEncoder(string filePath, [Media.VideoTrackAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackAttributes.html) videoAttrs, [Media.AudioTrackAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.AudioTrackAttributes.html) audioAttrs); 
## Declaration
public MediaEncoder(string filePath, [Media.VideoTrackEncoderAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes.html) videoAttrs, [Media.AudioTrackAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.AudioTrackAttributes.html) audioAttrs); 
## Declaration
public MediaEncoder(string filePath, [Media.VideoTrackAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackAttributes.html) videoAttrs); 
## Declaration
public MediaEncoder(string filePath, [Media.VideoTrackEncoderAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.VideoTrackEncoderAttributes.html) videoAttrs); 
## Declaration
public MediaEncoder(string filePath, AudioTrackAttributes[] audioAttrs); 
## Declaration
public MediaEncoder(string filePath, [Media.AudioTrackAttributes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Media.AudioTrackAttributes.html) audioAttrs); 
### Parameters
Parameter | Description  
---|---  
filePath | Path fo the media file to be written.  
videoAttrs | Attributes for the file's video track, if any.  
audioAttrs | Attributes for the file's audio tracks, if any.  
### Description
Create a new encoder with various track arrangements.
Throws exceptions when an error is encountered either with the format description or the creation of the file.
* * *
