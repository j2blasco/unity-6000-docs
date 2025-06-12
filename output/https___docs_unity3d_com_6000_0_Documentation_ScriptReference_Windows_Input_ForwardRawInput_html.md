* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Input.ForwardRawInput.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Input.html).ForwardRawInput
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
public static void ForwardRawInput(IntPtr rawInputHeaderIndices, IntPtr rawInputDataIndices, uint indicesCount, IntPtr rawInputData, uint rawInputDataSize); 
## Declaration
public static void ForwardRawInput(uint* rawInputHeaderIndices, uint* rawInputDataIndices, uint indicesCount, byte* rawInputData, uint rawInputDataSize); 
### Parameters
Parameter | Description  
---|---  
rawInputHeaderIndices | Pointer to array of indices that specify the byte offsets of RAWINPUTHEADER structures in rawInputData.  
rawInputDataIndices | Pointer to array of indices that specify the byte offsets of RAWINPUT::data field in rawInputData.  
indicesCount | Number of RAWINPUT events.  
rawInputData | Pointer to byte array containing RAWINPUT events.  
rawInputDataSize | RawInputData array size in bytes.  
### Description
Forwards raw input events to Unity.
On Windows, only one window per process can be registered to receive raw input events. This method allows you to forward raw input events to Unity if you overwrote Unity's raw input registration and you are receiving events yourself.  
  
The example below demonstrates how you can process raw input events yourself and optionally forward them to Unity.
```
using AOT;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.ComponentModel;
using System.Runtime.InteropServices;
using UnityEngine;  
  
public class InputRedirector : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
#if UNITY_EDITOR_WIN || UNITY_STANDALONE_WIN
    const ushort HID_USAGE_PAGE_GENERIC = 0x01;
    const ushort HID_USAGE_GENERIC_MOUSE = 0x02;
    const ushort HID_USAGE_GENERIC_KEYBOARD = 0x06;
    const uint WM_INPUT = 0x00FF;
    const uint RID_INPUT = 0x10000003;
    const int ERROR_INSUFFICIENT_BUFFER = 122;  
  
    const int RIM_TYPEMOUSE = 0;
    const int RIM_TYPEKEYBOARD = 1;
    const ushort kSpaceScanCode = 0x39;  
  
    struct WNDCLASSEXW
    {
        public int cbSize;
        public int style;
        public IntPtr lpfnWndProc;
        public int cbClsExtra;
        public int cbWndExtra;
        public IntPtr hInstance;
        public IntPtr hIcon;
        public IntPtr hCursor;
        public IntPtr hbrBackground;
        [MarshalAs(UnmanagedType.LPWStr)]
        public string lpszMenuName;
        [MarshalAs(UnmanagedType.LPWStr)]
        public string lpszClassName;
        public IntPtr hIconSm;
    }  
  
    struct RAWINPUTDEVICE
    {
        public ushort usUsagePage;
        public ushort usUsage;
        public uint dwFlags;
        public IntPtr hwndTarget;
    }  
  
    struct RAWINPUTHEADER
    {
        public uint dwType;
        public int dwSize;
        public IntPtr hDevice;
        public IntPtr wParam;
    }  
  
    struct RAWKEYBOARD
    {
        public ushort MakeCode;
        public RawKeyboardFlags Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html);
        public ushort Reserved;
        public ushort VKey;
        public uint Message[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Message.html);
        public uint ExtraInformation;
    }  
  
    [Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)]
    enum RawKeyboardFlags : ushort
    {
        RI_KEY_MAKE = 0,
        RI_KEY_BREAK = 1,
        RI_KEY_E0 = 2,
        RI_KEY_E1 = 4,
        RI_KEY_TERMSRV_SET_LED = 8,
        RI_KEY_TERMSRV_SHADOW = 0x10,
    }  
  

    [DllImport("kernel32.dll", SetLastError = true)]
    static extern IntPtr GetModuleHandleW([MarshalAs(UnmanagedType.LPWStr)] string lpModuleName);  
  
    [DllImport("kernel32.dll")]
    static extern IntPtr GetCurrentProcess();  
  
    [DllImport("kernel32.dll", SetLastError = true)]
    static extern bool IsWow64Process(IntPtr hProcess, out bool Wow64Process);  
  
    [DllImport("user32.dll", SetLastError = true)]
    [return : MarshalAs(UnmanagedType.U2)]
    static extern ushort RegisterClassExW([In] ref WNDCLASSEXW lpwcx);  
  
    [DllImport("user32.dll", SetLastError = true)]
    static extern bool UnregisterClassW(IntPtr windowClass, IntPtr hInstance);  
  
    [DllImport("user32.dll", SetLastError = true)]
    static extern IntPtr CreateWindowExW(uint dwExStyle, IntPtr windowClass, [MarshalAs(UnmanagedType.LPWStr)] string lpWindowName,
        uint dwStyle, int x, int y, int nWidth, int nHeight, IntPtr hWndParent, IntPtr hMenu, IntPtr hInstance, IntPtr pvParam);  
  
    [DllImport("user32.dll", SetLastError = true)]
    static extern bool DestroyWindow(IntPtr hWnd);  
  
    [DllImport("user32.dll")]
    static extern IntPtr DefWindowProcW(IntPtr hWnd, uint uMsg, IntPtr wParam, IntPtr lParam);  
  
    [DllImport("User32.dll", SetLastError = true)]
    static extern bool RegisterRawInputDevices([In][MarshalAs(UnmanagedType.LPArray)] RAWINPUTDEVICE[] pRawInputDevices, int uiNumDevices, int cbSize);  
  
    [DllImport("User32.dll", SetLastError = true)]
    static extern int GetRegisteredRawInputDevices([In][Out][MarshalAs(UnmanagedType.LPArray)] RAWINPUTDEVICE[] pRawInputDevices, ref int puiNumDevices, int cbSize);  
  
    [DllImport("User32.dll", SetLastError = true)]
    static extern int GetRawInputData(IntPtr hRawInput, uint uiCommand, [MarshalAs(UnmanagedType.LPArray)] byte[] pData, ref int pcbSize, int cbSizeHeader);  
  
    [DllImport("User32.dll", SetLastError = true)]
    static extern int GetRawInputBuffer([MarshalAs(UnmanagedType.LPArray)] byte[] pData, ref int pcbSize, int cbSizeHeader);  
  
    delegate IntPtr WndProcDelegate(IntPtr window, uint message, IntPtr wParam, IntPtr lParam);  
  
    static readonly WndProcDelegate s_WndProc = WndProc;
    static readonly int kRawInputHeaderSize = Marshal.SizeOf<RAWINPUTHEADER>();
    static readonly int kRawInputDeviceSize = Marshal.SizeOf<RAWINPUTDEVICE>();
    static readonly bool kIsWow64 = IsWow64();  
  
    static IntPtr s_HInstance = GetModuleHandleW(null);
    static byte[] s_RawInputBuffer = new byte[8192];
    static bool s_RedirectingInputToUnity = true;  
  
    static byte[] s_RawInputEvents = new byte[8192];
    static int[] s_RawInputHeaderIndices = new int[100];
    static int[] s_RawInputDataIndices = new int[100];  
  
    IntPtr m_WindowClass;
    IntPtr m_Hwnd;
    GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) m_TextStyle;  
  
    const int m_DeviceCount = 2;
    readonly RAWINPUTDEVICE[] m_Devices;
    RAWINPUTDEVICE[] m_QueryDevices;  
  
    public InputRedirector()
    {
        m_Devices = new RAWINPUTDEVICE[m_DeviceCount];
        m_QueryDevices = new RAWINPUTDEVICE[m_DeviceCount];
    }  
  
    private void RegisterRawInputDevices()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Registering raw input devices");  
  
        ref RAWINPUTDEVICE mouse = ref m_Devices[0];
        mouse.usUsagePage = HID_USAGE_PAGE_GENERIC;
        mouse.usUsage = HID_USAGE_GENERIC_MOUSE;
        mouse.hwndTarget = m_Hwnd;  
  
        ref RAWINPUTDEVICE keyboard = ref m_Devices[1];
        keyboard.usUsagePage = HID_USAGE_PAGE_GENERIC;
        keyboard.usUsage = HID_USAGE_GENERIC_KEYBOARD;
        keyboard.hwndTarget = m_Hwnd;  
  
        if (!RegisterRawInputDevices(m_Devices, m_DeviceCount, kRawInputDeviceSize))
            throw new Win32Exception(Marshal.GetLastWin32Error(), "Failed to register mouse and keyboard for Raw Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).");
    }  
  
    void Awake()
    {
        m_WindowClass = RegisterWindowClass();
        m_Hwnd = CreateWindowExW(0, m_WindowClass, "Raw Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) Redirection Window", 0, 0, 0, 0, 0, IntPtr.Zero, IntPtr.Zero, s_HInstance, IntPtr.Zero);
        if (m_Hwnd == null)
            throw new Win32Exception(Marshal.GetLastWin32Error(), "Failed to create raw input redirection window.");  
  
        RegisterRawInputDevices();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        int numberOfDevices = 0;
        GetRegisteredRawInputDevices(null, ref numberOfDevices, kRawInputDeviceSize);  
  
        if (m_QueryDevices.Length < numberOfDevices)
            Array.Resize(ref m_QueryDevices, numberOfDevices);  
  
        if (GetRegisteredRawInputDevices(m_QueryDevices, ref numberOfDevices, kRawInputDeviceSize) == -1)
        {
            var error = Marshal.GetLastWin32Error();
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("GetRegisteredRawInputDevices failed: " + new Win32Exception(error).Message[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Message.html));
        }
        else
        {
            for (int i = 0; i < numberOfDevices; i++)
            {
                if (m_QueryDevices[i].usUsage == HID_USAGE_GENERIC_MOUSE || m_QueryDevices[i].usUsage == HID_USAGE_GENERIC_KEYBOARD)
                {
                    if (m_QueryDevices[i].hwndTarget != m_Hwnd)
                    {
                        RegisterRawInputDevices();
                        break;
                    }
                }
            }
        }
    }  
  
    void OnDestroy()
    {
        if (!DestroyWindow(m_Hwnd))
            throw new Win32Exception(Marshal.GetLastWin32Error(), "Failed to destroy raw input redirection window class.");  
  
        if (!UnregisterClassW(m_WindowClass, s_HInstance))
            throw new Win32Exception(Marshal.GetLastWin32Error(), "Failed to unregister raw input redirection window class.");
    }  
  
    void OnGUI()
    {
        if (m_TextStyle == null)
        {
            m_TextStyle = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)(GUI.skin.label);
            m_TextStyle.fontSize = 24;
        }  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(100, 10, 500, 30), $"Redirecting input to Unity: {s_RedirectingInputToUnity}", m_TextStyle);
    }  
  
    [MonoPInvokeCallback(typeof(WndProcDelegate))]
    static IntPtr WndProc(IntPtr window, uint message, IntPtr wParam, IntPtr lParam)
    {
        try
        {
            if (message == WM_INPUT)
                ProcessRawInputMessage(lParam);  
  
            return DefWindowProcW(window, message, wParam, lParam);
        }
        catch (Exception e)
        {
            // Never let exception escape to native code as that will crash the app
            Debug.LogException[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogException.html)(e);
            return IntPtr.Zero;
        }
    }  
  
    static void ProcessRawInputMessage(IntPtr lParam)
    {
        int rawInputEventCount = 0;
        int rawInputEventsSize = 0;  
  
        // First, process the message we received
        int sizeofRawInputBuffer = s_RawInputBuffer.Length;
        int result = GetRawInputData(lParam, RID_INPUT, s_RawInputBuffer, ref sizeofRawInputBuffer, kRawInputHeaderSize);
        if (result == -1)
        {
            var errorCode = Marshal.GetLastWin32Error();
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)($"Failed to get raw input data: {new Win32Exception(errorCode).Message[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Message.html)}");
            return;
        }  
  
        CopyEventFromRawInputBuffer(0, kRawInputHeaderSize, ref rawInputEventCount, ref rawInputEventsSize);  
  
        // Next, drain the raw input message queue so they don't keep getting
        // pumped one at a time through PeekMessage/DispatchMessage as that is
        // too slow with high input polling rate devices
        while (true)
        {
            var rawInputCount = GetRawInputBuffer(s_RawInputBuffer, ref sizeofRawInputBuffer, kRawInputHeaderSize);
            if (rawInputCount == 0)
                break;  
  
            if (rawInputCount == -1)
            {
                var errorCode = Marshal.GetLastWin32Error();
                Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)($"Failed to get raw input buffer: {new Win32Exception(errorCode).Message[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Message.html)}");
                break;
            }  
  
            int offset = 0;
            for (int i = 0; i < rawInputCount; i++)
            {
                var rawInputDataOffset = kRawInputHeaderSize;  
  
                if (kIsWow64)
                {
                    // RAWINPUTHEADER is 16 bytes on 32-bit, but 24 bytes on 64-bit. Since this data is memcpy-ed from the kernel,
                    // we need to adjust the data pointer by 8 bytes if we're in a 32-bit process but 64-bit kernel.
                    // We only need to do this with data coming from GetRawInputBuffer as GetRawInputData fixes up the single
                    // event it returns.
                    rawInputDataOffset += rawInputDataOffset;
                }  
  
                offset += CopyEventFromRawInputBuffer(offset, rawInputDataOffset, ref rawInputEventCount, ref rawInputEventsSize);
            }
        }  
  
        // Finally, dispatch the events to Unity
        if (s_RedirectingInputToUnity)
        {
            unsafe
            {
                fixed(int* rawInputHeaderIndices = s_RawInputHeaderIndices)
                {
                    fixed(int* rawInputDataIndices = s_RawInputDataIndices)
                    {
                        fixed(byte* rawInputData = s_RawInputEvents)
                        {
                            UnityEngine.Windows.Input.ForwardRawInput((uint*)rawInputHeaderIndices, (uint*)rawInputDataIndices, (uint)rawInputEventCount, rawInputData, (uint)rawInputEventsSize);
                        }
                    }
                }
            }
        }
    }  
  
    private static int CopyEventFromRawInputBuffer(int offset, int dataOffset, ref int rawInputEventCount, ref int rawInputEventsSize)
    {
        RAWINPUTHEADER header;
        unsafe
        {
            fixed(byte* rawInputBufferPtr = s_RawInputBuffer)
            header = *(RAWINPUTHEADER*)(rawInputBufferPtr + offset);
        }  
  
        if (header.dwType == RIM_TYPEKEYBOARD)
        {
            unsafe
            {
                fixed(byte* rawInputBufferPtr = s_RawInputBuffer)
                {
                    var keyboard = *(RAWKEYBOARD*)(rawInputBufferPtr + dataOffset);  
  
                    // Releasing space key will toggle whether we forward events to Unity
                    bool keyPressed = (keyboard.Flags & RawKeyboardFlags.RI_KEY_BREAK) == 0;
                    if (!keyPressed && keyboard.MakeCode == kSpaceScanCode)
                        s_RedirectingInputToUnity = !s_RedirectingInputToUnity;
                }
            }
        }  
  
        if (rawInputEventsSize + header.dwSize > s_RawInputEvents.Length)
            Array.Resize(ref s_RawInputEvents, Math.Max(rawInputEventsSize + header.dwSize, 2 * s_RawInputEvents.Length));  
  
        if (rawInputEventCount == s_RawInputHeaderIndices.Length)
        {
            Array.Resize(ref s_RawInputHeaderIndices, 2 * s_RawInputHeaderIndices.Length);
            Array.Resize(ref s_RawInputDataIndices, 2 * s_RawInputHeaderIndices.Length);
        }  
  
        s_RawInputHeaderIndices[rawInputEventCount] = rawInputEventsSize;
        s_RawInputDataIndices[rawInputEventCount] = rawInputEventsSize + dataOffset;
        Array.Copy(s_RawInputBuffer, offset, s_RawInputEvents, rawInputEventsSize, header.dwSize);  
  
        rawInputEventCount++;
        rawInputEventsSize += header.dwSize;
        return header.dwSize;
    }  
  
    static IntPtr RegisterWindowClass()
    {
        var wndClass = new WNDCLASSEXW();
        wndClass.cbSize = Marshal.SizeOf<WNDCLASSEXW>();
        wndClass.lpfnWndProc = Marshal.GetFunctionPointerForDelegate(s_WndProc);
        wndClass.hInstance = s_HInstance;
        wndClass.lpszClassName = "RawInputRedirector";  
  
        var registeredClass = RegisterClassExW(ref wndClass);
        if (registeredClass == 0)
            throw new Win32Exception(Marshal.GetLastWin32Error(), "Failed to register the window class.");  
  
        return new IntPtr(registeredClass);
    }  
  
    private static bool IsWow64()
    {
        if (IntPtr.Size == 8)
            return false;  
  
        if (!IsWow64Process(GetCurrentProcess(), out bool isWow64))
            throw new Win32Exception(Marshal.GetLastWin32Error(), "Failed to figure out whether we're running under WOW64.");  
  
        return isWow64;
    }  
  
#endif // UNITY_EDITOR_WIN || UNITY_STANDALONE_WIN
}

```

* * *
