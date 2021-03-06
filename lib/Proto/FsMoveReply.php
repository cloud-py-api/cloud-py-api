<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fs.proto

namespace OCA\Cloud_Py_API\Proto;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>OCA.Cloud_Py_API.Proto.FsMoveReply</code>
 */
class FsMoveReply extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>.OCA.Cloud_Py_API.Proto.fsResultCode resCode = 1;</code>
     */
    protected $resCode = 0;
    /**
     * Generated from protobuf field <code>.OCA.Cloud_Py_API.Proto.fsId fileId = 2;</code>
     */
    protected $fileId = null;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type int $resCode
     *     @type \OCA\Cloud_Py_API\Proto\fsId $fileId
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Fs::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>.OCA.Cloud_Py_API.Proto.fsResultCode resCode = 1;</code>
     * @return int
     */
    public function getResCode()
    {
        return $this->resCode;
    }

    /**
     * Generated from protobuf field <code>.OCA.Cloud_Py_API.Proto.fsResultCode resCode = 1;</code>
     * @param int $var
     * @return $this
     */
    public function setResCode($var)
    {
        GPBUtil::checkEnum($var, \OCA\Cloud_Py_API\Proto\fsResultCode::class);
        $this->resCode = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>.OCA.Cloud_Py_API.Proto.fsId fileId = 2;</code>
     * @return \OCA\Cloud_Py_API\Proto\fsId|null
     */
    public function getFileId()
    {
        return $this->fileId;
    }

    public function hasFileId()
    {
        return isset($this->fileId);
    }

    public function clearFileId()
    {
        unset($this->fileId);
    }

    /**
     * Generated from protobuf field <code>.OCA.Cloud_Py_API.Proto.fsId fileId = 2;</code>
     * @param \OCA\Cloud_Py_API\Proto\fsId $var
     * @return $this
     */
    public function setFileId($var)
    {
        GPBUtil::checkMessage($var, \OCA\Cloud_Py_API\Proto\fsId::class);
        $this->fileId = $var;

        return $this;
    }

}

