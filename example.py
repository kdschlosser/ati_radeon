# -*- coding: utf-8 -*-
#
# ***********************************************************************************
# MIT License
#
# Copyright (c) 2020 Kevin G. Schlosser
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# ***********************************************************************************

from __future__ import print_function
import pyamd_adl

for adapter in pyamd_adl.adapters:
    print('id:', adapter.id)
    print('name:', adapter.name)
    print('index:', adapter.index)
    print('device_number:', adapter.device_number)
    print('bus_number:', adapter.bus_number)
    print('vendor_id:', adapter.vendor_id)
    print('supports_edid_management:', adapter.supports_edid_management)
    print('is_overdrive_enabled:', adapter.is_overdrive_enabled)
    print('is_overdrive_supported:', adapter.is_overdrive_supported)
    print('overdrive_version:', adapter.overdrive_version)
    print('supported_aspects:', adapter.supported_aspects)
    print('udid:', adapter.udid)
    print('function_number:', adapter.function_number)
    print('is_present:', adapter.is_present)
    print('exists:', adapter.exists)
    print('driver_path:', adapter.driver_path)
    print('driver_path_ext:', adapter.driver_path_ext)
    print('upnp_path:', adapter.upnp_path)
    print('display_index:', adapter.display_index)
    print('driver_index:', adapter.driver_index)
    print('screen_config_name:', adapter.screen_config_name)
    print('asic_family_type:', adapter.asic_family_type)
    print('can_change_speed:', adapter.can_change_speed)
    print('speed:', adapter.speed)
    print('default_speed:', adapter.default_speed)
    print('is_gpu_accessable:', adapter.is_gpu_accessable)
    print('is_power_control_supported:', adapter.is_power_control_supported)
    print('bus_speed:', adapter.bus_speed)
    print('bus_lanes:', adapter.bus_lanes)
    print('max_bus_lanes:', adapter.bus_lanes.max)
    print()
    print('power_control')
    power_control = adapter.power_control
    print('    value:', power_control)
    print('    min:', power_control.min)
    print('    max:', power_control.max)
    print('    step:', power_control.step)
    print('    default:', power_control.default)
    print()
    print('temperatures')
    temperatures = adapter.temperatures
    for temperature in temperatures:
        print('   :', temperature)

    print()
    print('fan_speeds')
    for fan_speed in adapter.fan_speeds:
        print('    speed:', fan_speed, fan_speed.unit_of_measure)
        print('    min:', fan_speed.min, fan_speed.unit_of_measure)
        print('    max:', fan_speed.max, fan_speed.unit_of_measure)
        print('    automatic:', fan_speed.automatic)
        print()

    print()
    print('firmware')
    firmware = adapter.firmware
    print('    date:', firmware.date)
    print('    part_number:', firmware.part_number)
    print('    version:', firmware.version)

    print()
    print('core')
    core = adapter.core
    voltages = core.voltages
    clocks = core.clocks
    actual_clock = clocks.actual
    actual_voltage = voltages.actual
    load = core.load
    print('    actual clock:', actual_clock, actual_clock.unit_of_measure)
    print('    actual voltage:', actual_voltage, actual_voltage.unit_of_measure)
    print('    load:', load, load.unit_of_measure)
    print()
    print('    clocks')
    for clock in clocks:
        print('        clock:', clock, clock.unit_of_measure)
        print('        step:', clock.step, clock.unit_of_measure)
        print('        default:', clock.default, clock.unit_of_measure)
        print('        min:', clock.min, clock.unit_of_measure)
        print('        max:', clock.max, clock.unit_of_measure)
        print('        is_active:', clock.is_active)
        print()

    print()
    print('    voltages')
    for voltage in voltages:
        print('        clock:', voltage, voltage.unit_of_measure)
        print('        step:', voltage.step, voltage.unit_of_measure)
        print('        default:', voltage.default, voltage.unit_of_measure)
        print('        min:', voltage.min, voltage.unit_of_measure)
        print('        max:', voltage.max, voltage.unit_of_measure)
        print('        is_active:', voltage.is_active)
        print()

    print()
    print('memory')
    memory = adapter.memory
    clocks = memory.clocks
    actual_clock = clocks.actual
    print('    size:', memory.size)
    print('    type:', memory.type)
    print('    bandwidth:', memory.bandwidth)
    print('    actual_clock:', actual_clock, actual_clock.unit_of_measure)

    print()
    print('    clocks')
    for clock in clocks:
        print('        clock:', clock, clock.unit_of_measure)
        print('        step:', clock.step, clock.unit_of_measure)
        print('        default:', clock.default, clock.unit_of_measure)
        print('        min:', clock.min, clock.unit_of_measure)
        print('        max:', clock.max, clock.unit_of_measure)
        print('        is_active:', clock.is_active)
        print()

    print()
    print('crossfire')
    crossfire = adapter.crossfire
    print('    is_prefered_adapter:', crossfire.is_prefered_adapter)
    print('    is_combination_supported:', crossfire.is_combination_supported)
    print('    state:', crossfire.state)

    print()
    print('crossdisplay')
    crossdisplay = adapter.crossdisplay

    print()
    print('fps')
    fps = adapter.fps
    print('    is_supported:', fps.is_supported)
    print('    version:', fps.version)
    print('    type:', fps.type)
    print('    is_enabled:', fps.is_enabled)
    print('    value:', fps.value)
    print('    maximum:', fps.maximum)
    print('    minimum:', fps.minimum)

    print()
    print('error_records')
    error_records = adapter.error_records
    for i, record in enumerate(error_records):
        print('    record_number:', i)
        print('    severity:', record.severity)
        print('    is_count_valid:', record.is_count_valid)
        print('    count:', record.count)
        print('    is_valid_location:', record.is_location_valid)
        print('    cu:', record.cu)
        print('    location_name:', record.location_name)
        print('    timestamp:', record.timestamp)
        print()

    print()
    print('connectors')
    print()

    for connector in adapter:
        print('    type:', connector.type)
        print('    index:', connector.index)

        print()
        print('    display')
        display = connector.display
        if display is None:
            print('        None')
        else:
            print('        name:', display.name)
            print('        manufacturer:', display.manufacturer)
            print('        type:', display.type)
            print('        output_type:', display.output_type)
            print('        is_preserve_aspect_ratio_supported:', display.is_preserve_aspect_ratio_supported)
            print('        preserve_aspect_ratio_default:', display.preserve_aspect_ratio_default)
            print('        preserve_aspect_ratio:', display.preserve_aspect_ratio)
            print('        is_image_expansion_supported:', display.is_image_expansion_supported)
            print('        image_expansion_default:', display.image_expansion_default)
            print('        image_expansion:', display.image_expansion)
            print('        dither:', display.dither)
            print('        supported_pixel_formats:', display.supported_pixel_formats)
            print('        pixel_format:', display.pixel_format)
            print('        adjustment_coherent_default:', display.adjustment_coherent_default)
            print('        adjustment_coherent:', display.adjustment_coherent)
            print('        reduced_blanking_default:', display.reduced_blanking_default)
            print('        reduced_blanking:', display.reduced_blanking)
            print('        formats_override_supported:', display.formats_override_supported)
            print('        formats_override_supported_ex:', display.formats_override_supported_ex)
            print('        formats_override:', display.formats_override)
            print('        supported_color_depths:', display.supported_color_depths)
            print('        color_depth:', display.color_depth)
            print('        is_gpu_scaling_supported:', display.is_gpu_scaling_supported)
            print('        gpu_scaling_default:', display.gpu_scaling_default)
            print('        gpu_scaling:', display.gpu_scaling)
            print('        supported_contents:', display.supported_contents)
            print('        content:', display.content)
            print('        is_virtual_super_resolution_supported:', display.is_virtual_super_resolution_supported)
            print('        virtual_super_resolution:', display.virtual_super_resolution)
            print('        is_expansion_mode_supported:', display.is_expansion_mode_supported)
            print('        expansion_mode:', display.expansion_mode)

            print()
            print('        is_freesync_supported:', display.is_freesync_supported)
            freesync = display.freesync
            print('        freesync')
            print('            mode:', freesync.mode)
            print('            default_mode:', freesync.default_mode)
            print('            min_refresh:', freesync.min_refresh)
            print('            max_refresh:', freesync.max_refresh)

            print()
            deflicker = display.deflicker
            print('        deflicker')
            print('            value:', deflicker)
            print('            default:', deflicker.default)
            print('            min:', deflicker.min)
            print('            max:', deflicker.max)
            print('            step:', deflicker.step)

            print()
            filter_svideo = display.filter_svideo
            print('        filter_svideo')
            print('            value:', filter_svideo)
            print('            default:', filter_svideo.default)
            print('            min:', filter_svideo.min)
            print('            max:', filter_svideo.max)
            print('            step:', filter_svideo.step)

            print()
            print('        is_brightness_supported:', display.is_brightness_supported)
            brightness = display.brightness
            print('        brightness')
            print('            value:', brightness)
            print('            default:', brightness.default)
            print('            min:', brightness.min)
            print('            max:', brightness.max)
            print('            step:', brightness.step)

            print()
            print('        is_contrast_supported:', display.is_contrast_supported)
            contrast = display.contrast
            print('        contrast')
            print('            value:', contrast)
            print('            default:', contrast.default)
            print('            min:', contrast.min)
            print('            max:', contrast.max)
            print('            step:', contrast.step)

            print()
            print('        is_saturation_supported:', display.is_saturation_supported)
            saturation = display.saturation
            print('        saturation')
            print('            value:', saturation)
            print('            default:', saturation.default)
            print('            min:', saturation.min)
            print('            max:', saturation.max)
            print('            step:', saturation.step)

            print()
            print('        is_hue_supported:', display.is_hue_supported)
            hue = display.hue
            print('        hue')
            print('            value:', hue)
            print('            default:', hue.default)
            print('            min:', hue.min)
            print('            max:', hue.max)
            print('            step:', hue.step)

            print()
            print('        is_color_temperature_supported:', display.is_color_temperature_supported)
            print('        color_temperature_source:', display.color_temperature_source)
            print('        color_temperature_source_default:', display.color_temperature_source_default)
            color_temperature = display.color_temperature
            print('        color_temperature')
            print('            value:', color_temperature)
            print('            default:', color_temperature.default)
            print('            min:', color_temperature.min)
            print('            max:', color_temperature.max)
            print('            step:', color_temperature.step)

            print()
            print('        is_overscan_supported:', display.is_overscan_supported)
            overscan = display.overscan
            print('        overscan')
            print('            value:', overscan)
            print('            default:', overscan.default)
            print('            min:', overscan.min)
            print('            max:', overscan.max)
            print('            step:', overscan.step)

            print()
            print('        is_underscan_supported:', display.is_underscan_supported)
            underscan = display.underscan
            print('        underscan')
            print('            value:', underscan)
            print('            default:', underscan.default)
            print('            min:', underscan.min)
            print('            max:', underscan.max)
            print('            step:', underscan.step)

            print()
            position = display.position
            print('        position')
            print('            is_horizontal_position_supported:', position.is_horizontal_position_supported)
            x = position.x
            print('            x')
            print('                value:', x)
            print('                default:', x.default)
            print('                min:', x.min)
            print('                max:', x.max)
            print('                step:', x.step)

            print()
            print('            is_vertical_position_supported:', position.is_vertical_position_supported)
            y = position.y
            print('            y')
            print('                value:', y)
            print('                default:', y.default)
            print('                min:', y.min)
            print('                max:', y.max)
            print('                step:', y.step)

            print()
            size = display.size
            print('        size')
            print('            is_horizontal_size_supported:', size.is_horizontal_size_supported)
            width = size.width
            print('            width')
            print('                value:', width)
            print('                default:', width.default)
            print('                min:', width.min)
            print('                max:', width.max)
            print('                step:', width.step)

            print()
            print('            is_vertical_size_supported:', size.is_vertical_size_supported)
            height = size.height
            print('            height')
            print('                value:', height)
            print('                default:', height.default)
            print('                min:', height.min)
            print('                max:', height.max)
            print('                step:', height.step)

        print()
        print('    supported_connections')
        for supported_connection in connector:
            print('        name:', supported_connection.name)
            print('        supports_bitrate:', supported_connection.supports_bitrate)
            print('        supports_number_of_lanes:', supported_connection.supports_number_of_lanes)
            print('        supports_three_d_caps:', supported_connection.supports_three_d_caps)
            print('        supports_output_bandwidth:', supported_connection.supports_output_bandwidth)
            print('        supports_color_depth:', supported_connection.supports_color_depth)
            print('        is_connected:', supported_connection.is_connected)
            print('        bitrate:', supported_connection.bitrate)
            print('        number_of_lanes:', supported_connection.number_of_lanes)
            print('        three_d_caps:', supported_connection.three_d_caps)
            print('        output_bandwidth:', supported_connection.output_bandwidth)
            print('        color_depth:', supported_connection.color_depth)
            print()

    print('\n\n')


