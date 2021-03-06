<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto

namespace OCA\Cloud_Py_API\Proto;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>OCA.Cloud_Py_API.Proto.DbSelectReply</code>
 */
class DbSelectReply extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>int64 rowCount = 1;</code>
     */
    protected $rowCount = 0;
    /**
     * Generated from protobuf field <code>string error = 2;</code>
     */
    protected $error = '';
    /**
     *valid if only rowcount > 0.
     *
     * Generated from protobuf field <code>string handle = 3;</code>
     */
    protected $handle = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type int|string $rowCount
     *     @type string $error
     *     @type string $handle
     *          valid if only rowcount > 0.
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Db::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>int64 rowCount = 1;</code>
     * @return int|string
     */
    public function getRowCount()
    {
        return $this->rowCount;
    }

    /**
     * Generated from protobuf field <code>int64 rowCount = 1;</code>
     * @param int|string $var
     * @return $this
     */
    public function setRowCount($var)
    {
        GPBUtil::checkInt64($var);
        $this->rowCount = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string error = 2;</code>
     * @return string
     */
    public function getError()
    {
        return $this->error;
    }

    /**
     * Generated from protobuf field <code>string error = 2;</code>
     * @param string $var
     * @return $this
     */
    public function setError($var)
    {
        GPBUtil::checkString($var, True);
        $this->error = $var;

        return $this;
    }

    /**
     *valid if only rowcount > 0.
     *
     * Generated from protobuf field <code>string handle = 3;</code>
     * @return string
     */
    public function getHandle()
    {
        return $this->handle;
    }

    /**
     *valid if only rowcount > 0.
     *
     * Generated from protobuf field <code>string handle = 3;</code>
     * @param string $var
     * @return $this
     */
    public function setHandle($var)
    {
        GPBUtil::checkString($var, True);
        $this->handle = $var;

        return $this;
    }

}

