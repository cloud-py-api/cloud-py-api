<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto

namespace OCA\Cloud_Py_API\Proto\DbCursorReply;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>OCA.Cloud_Py_API.Proto.DbCursorReply.columnData</code>
 */
class columnData extends \Google\Protobuf\Internal\Message
{
    /**
     *if result is NULL for that column raw, then this is True.
     *
     * Generated from protobuf field <code>bool present = 1;</code>
     */
    protected $present = false;
    /**
     *present if result fir column raw is not NULL.
     *
     * Generated from protobuf field <code>bytes data = 2;</code>
     */
    protected $data = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type bool $present
     *          if result is NULL for that column raw, then this is True.
     *     @type string $data
     *          present if result fir column raw is not NULL.
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Db::initOnce();
        parent::__construct($data);
    }

    /**
     *if result is NULL for that column raw, then this is True.
     *
     * Generated from protobuf field <code>bool present = 1;</code>
     * @return bool
     */
    public function getPresent()
    {
        return $this->present;
    }

    /**
     *if result is NULL for that column raw, then this is True.
     *
     * Generated from protobuf field <code>bool present = 1;</code>
     * @param bool $var
     * @return $this
     */
    public function setPresent($var)
    {
        GPBUtil::checkBool($var);
        $this->present = $var;

        return $this;
    }

    /**
     *present if result fir column raw is not NULL.
     *
     * Generated from protobuf field <code>bytes data = 2;</code>
     * @return string
     */
    public function getData()
    {
        return $this->data;
    }

    /**
     *present if result fir column raw is not NULL.
     *
     * Generated from protobuf field <code>bytes data = 2;</code>
     * @param string $var
     * @return $this
     */
    public function setData($var)
    {
        GPBUtil::checkString($var, False);
        $this->data = $var;

        return $this;
    }

}

// Adding a class alias for backwards compatibility with the previous class name.
class_alias(columnData::class, \OCA\Cloud_Py_API\Proto\DbCursorReply_columnData::class);

