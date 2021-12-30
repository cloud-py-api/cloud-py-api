<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core.proto

namespace Cloud_Py_API\DbExecRequest;

use UnexpectedValueException;

/**
 * Protobuf type <code>Cloud_Py_API.DbExecRequest.rType</code>
 */
class rType
{
    /**
     * Generated from protobuf enum <code>INSERT = 0;</code>
     */
    const INSERT = 0;
    /**
     * Generated from protobuf enum <code>UPDATE = 1;</code>
     */
    const UPDATE = 1;
    /**
     * Generated from protobuf enum <code>DELETE = 2;</code>
     */
    const DELETE = 2;

    private static $valueToName = [
        self::INSERT => 'INSERT',
        self::UPDATE => 'UPDATE',
        self::DELETE => 'DELETE',
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
class_alias(rType::class, \Cloud_Py_API\DbExecRequest_rType::class);
