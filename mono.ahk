	#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
^#!m::
toggle_mono() {
	send #i
	sleep 500
	Send {Tab}{Right 9}{Enter}
	sleep 500
	Send {Tab}{Down 7}{Enter}
	sleep 500
	send {Tab 4}{Space}
	sleep 100
	send !{F4}
}
