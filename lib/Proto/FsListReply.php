<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fs.proto

namespace OCA\Cloud_Py_API\Proto;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>OCA.Cloud_Py_API.Proto.FsListReply</code>
 */
class FsListReply extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>repeated .OCA.Cloud_Py_API.Proto.FsNodeInfo nodes = 1;</code>
     */
    private $nodes;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type \OCA\Cloud_Py_API\Proto\FsNodeInfo[]|\Google\Protobuf\Internal\RepeatedField $nodes
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Fs::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>repeated .OCA.Cloud_Py_API.Proto.FsNodeInfo nodes = 1;</code>
     * @return \Google\Protobuf\Internal\RepeatedField
     */
    public function getNodes()
    {
        return $this->nodes;
    }

    /**
     * Generated from protobuf field <code>repeated .OCA.Cloud_Py_API.Proto.FsNodeInfo nodes = 1;</code>
     * @param \OCA\Cloud_Py_API\Proto\FsNodeInfo[]|\Google\Protobuf\Internal\RepeatedField $var
     * @return $this
     */
    public function setNodes($var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::MESSAGE, \OCA\Cloud_Py_API\Proto\FsNodeInfo::class);
        $this->nodes = $arr;

        return $this;
    }

}

