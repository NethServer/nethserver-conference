==================
nethserver-conference
==================

Nethserver conference's configurations.

Properties:

* ``JitsiUrl``: The location of the Jitsi Meet instance, this property can be
  used as base path by services that want to integrate Jitsi Meet as conference engine.

Example: ::

 conference=configuration
    JitsiUrl=https://jitsi.example.com

Configure a Jitsi Meet instance
-------------------------------

After setting the ``JitsiUrl`` property, a ``nethserver-conference-save`` event
must be invoked to inform the subscribed services about the modification.

Example: ::

 config setprop conference JitsiUrl https://jitsi.example.com
 signal-event nethserver-conference-save
