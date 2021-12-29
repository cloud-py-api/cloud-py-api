<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core.proto

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>DbCursor</code>
 */
class DbCursor extends \Google\Protobuf\Internal\Message
{
    /**
     *msgClass.DB_CURSOR
     *
     * Generated from protobuf field <code>.msgClass classId = 1;</code>
     */
    protected $classId = 0;
    /**
     * Generated from protobuf field <code>int64 handle = 2;</code>
     */
    protected $handle = 0;
    /**
     * Generated from protobuf field <code>.dbCursorCmd cmd = 3;</code>
     */
    protected $cmd = 0;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type int $classId
     *          msgClass.DB_CURSOR
     *     @type int|string $handle
     *     @type int $cmd
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Proto\Core::initOnce();
        parent::__construct($data);
    }

    /**
     *msgClass.DB_CURSOR
     *
     * Generated from protobuf field <code>.msgClass classId = 1;</code>
     * @return int
     */
    public function getClassId()
    {
        return $this->classId;
    }

    /**
     *msgClass.DB_CURSOR
     *
     * Generated from protobuf field <code>.msgClass classId = 1;</code>
     * @param int $var
     * @return $this
     */
    public function setClassId($var)
    {
        GPBUtil::checkEnum($var, \msgClass::class);
        $this->classId = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>int64 handle = 2;</code>
     * @return int|string
     */
    public function getHandle()
    {
        return $this->handle;
    }

    /**
     * Generated from protobuf field <code>int64 handle = 2;</code>
     * @param int|string $var
     * @return $this
     */
    public function setHandle($var)
    {
        GPBUtil::checkInt64($var);
        $this->handle = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>.dbCursorCmd cmd = 3;</code>
     * @return int
     */
    public function getCmd()
    {
        return $this->cmd;
    }

    /**
     * Generated from protobuf field <code>.dbCursorCmd cmd = 3;</code>
     * @param int $var
     * @return $this
     */
    public function setCmd($var)
    {
        GPBUtil::checkEnum($var, \dbCursorCmd::class);
        $this->cmd = $var;

        return $this;
    }

}
