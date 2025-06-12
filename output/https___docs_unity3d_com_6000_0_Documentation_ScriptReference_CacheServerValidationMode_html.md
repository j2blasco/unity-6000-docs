* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerValidationMode.html

# CacheServerValidationMode
enumeration
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
### Description
Options for the accelerate server validation mode.
Use this enum with [EditorSettings.cacheServerValidationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorSettings-cacheServerValidationMode.html) to select the Accelerator server validation mode for the project. Used in conjunction with the Accelerator server [Accelerator server](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityAccelerator.html) settings ProtobufBlobHashRequired ProtobufBlobHashValidateGets and ProtobufBlobHashValidatePuts.
### Properties
Property | Description  
---|---  
[Disabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerValidationMode.Disabled.html) | Disable validation for the cache server.  
[UploadOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerValidationMode.UploadOnly.html) | Calculate content hashes for uploaded artifacts and send them to the Accelerator for validation.  
[Enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerValidationMode.Enabled.html) | Calculate and upload hashes. Validate Accelerator-provided hashes during downloads.  
[Required](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServerValidationMode.Required.html) | Calculate and uploaded content hashes to the Accelerator. Require Accelerator-provided hashes for download validation.  
* * *
