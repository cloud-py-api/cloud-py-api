<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto

namespace OCA\Cloud_Py_API\Proto\DbCursorRequest;

use UnexpectedValueException;

/**
 * Protobuf type <code>OCA.Cloud_Py_API.Proto.DbCursorRequest.cCmd</code>
 */
class cCmd
{
    /**
     * Generated from protobuf enum <code>FETCH = 0;</code>
     */
    const FETCH = 0;
    /**
     * Generated from protobuf enum <code>FETCH_ALL = 1;</code>
     */
    const FETCH_ALL = 1;
    /**
     * Generated from protobuf enum <code>CLOSE = 2;</code>
     */
    const CLOSE = 2;

    private static $valueToName = [
        self::FETCH => 'FETCH',
        self::FETCH_ALL => 'FETCH_ALL',
        self::CLOSE => 'CLOSE',
    ];

    public static function name($value)
    {
        if (!isset(self::$valueToName[$value])) {
            throw new UnexpectedValueException(sprintf(
                    'Enum %s has no name defined for value %s', __CLASS__, $value));
        }
        return self::$valueToName[$value];
    }


    public static function value($name)
    {
        $const = __CLASS__ . '::' . strtoupper($name);
        if (!defined($const)) {
            throw new UnexpectedValueException(sprintf(
                    'Enum %s has no value defined for name %s', __CLASS__, $name));
        }
        return constant($const);
    }
}

// Adding a class alias for backwards compatibility with the previous class name.
class_alias(cCmd::class, \OCA\Cloud_Py_API\Proto\DbCursorRequest_cCmd::class);

