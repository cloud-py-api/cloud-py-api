<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core.proto

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>FsGetInfo</code>
 */
class FsGetInfo extends \Google\Protobuf\Internal\Message
{
    /**
     *msgClass.FS_GET_INFO
     *
     * Generated from protobuf field <code>.msgClass classId = 1;</code>
     */
    protected $classId = 0;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type int $classId
     *          msgClass.FS_GET_INFO
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Proto\Core::initOnce();
        parent::__construct($data);
    }

    /**
     *msgClass.FS_GET_INFO
     *
     * Generated from protobuf field <code>.msgClass classId = 1;</code>
     * @return int
     */
    public function getClassId()
    {
        return $this->classId;
    }

    /**
     *msgClass.FS_GET_INFO
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

}
