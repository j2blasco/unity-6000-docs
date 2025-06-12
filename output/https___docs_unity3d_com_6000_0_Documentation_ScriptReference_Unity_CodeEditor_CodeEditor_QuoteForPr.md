* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.QuoteForProcessStart.html

#  [CodeEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.CodeEditor.CodeEditor.html).QuoteForProcessStart
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
public static string QuoteForProcessStart(string argument); 
### Description
Quotes a string to pass to Process.Start as a single argument, and appends it to this string builder.
On Windows systems, quote using the Win32 CommandLineToArgvW API scheme. Most Windows applications use this scheme, although there are exceptions (for example, cmd.exe and cscript.exe).  
  
On Unix-based systems, quote using the GLib g_shell_parse_argv function that Mono uses. This function converts the argument string to a native Unix argument list.  
  
Command line shells such as cmd.exe and the POSIX shell may use distinct quotation mechanisms. Do not use the QuoteForProcessStart method to quote arguments for command line shells.  
  
Do not append two quoted arguments to the string builder without putting an unquoted separator between them. Consecutive quotation marks trigger unpredictable behavior in CommandLineToArgvW, and may also trigger undocumented behavior other argument processors. 
* * *
