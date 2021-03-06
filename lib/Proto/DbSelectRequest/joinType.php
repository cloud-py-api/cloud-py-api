<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto

namespace OCA\Cloud_Py_API\Proto\DbSelectRequest;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>OCA.Cloud_Py_API.Proto.DbSelectRequest.joinType</code>
 */
class joinType extends \Google\Protobuf\Internal\Message
{
    /**
     *join, innerJoin, leftJoin, rightJoin.
     *
     * Generated from protobuf field <code>string name = 1;</code>
     */
    protected $name = '';
    /**
     * Generated from protobuf field <code>string fromAlias = 2;</code>
     */
    protected $fromAlias = '';
    /**
     * Generated from protobuf field <code>string join = 3;</code>
     */
    protected $join = '';
    /**
     * Generated from protobuf field <code>string alias = 4;</code>
     */
    protected $alias = '';
    /**
     * Generated from protobuf field <code>string condition = 5;</code>
     */
    protected $condition = '';

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $name
     *          join, innerJoin, leftJoin, rightJoin.
     *     @type string $fromAlias
     *     @type string $join
     *     @type string $alias
     *     @type string $condition
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Db::initOnce();
        parent::__construct($data);
    }

    /**
     *join, innerJoin, leftJoin, rightJoin.
     *
     * Generated from protobuf field <code>string name = 1;</code>
     * @return string
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     *join, innerJoin, leftJoin, rightJoin.
     *
     * Generated from protobuf field <code>string name = 1;</code>
     * @param string $var
     * @return $this
     */
    public function setName($var)
    {
        GPBUtil::checkString($var, True);
        $this->name = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string fromAlias = 2;</code>
     * @return string
     */
    public function getFromAlias()
    {
        return $this->fromAlias;
    }

    /**
     * Generated from protobuf field <code>string fromAlias = 2;</code>
     * @param string $var
     * @return $this
     */
    public function setFromAlias($var)
    {
        GPBUtil::checkString($var, True);
        $this->fromAlias = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string join = 3;</code>
     * @return string
     */
    public function getJoin()
    {
        return $this->join;
    }

    /**
     * Generated from protobuf field <code>string join = 3;</code>
     * @param string $var
     * @return $this
     */
    public function setJoin($var)
    {
        GPBUtil::checkString($var, True);
        $this->join = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string alias = 4;</code>
     * @return string
     */
    public function getAlias()
    {
        return $this->alias;
    }

    /**
     * Generated from protobuf field <code>string alias = 4;</code>
     * @param string $var
     * @return $this
     */
    public function setAlias($var)
    {
        GPBUtil::checkString($var, True);
        $this->alias = $var;

        return $this;
    }

    /**
     * Generated from protobuf field <code>string condition = 5;</code>
     * @return string
     */
    public function getCondition()
    {
        return $this->condition;
    }

    /**
     * Generated from protobuf field <code>string condition = 5;</code>
     * @param string $var
     * @return $this
     */
    public function setCondition($var)
    {
        GPBUtil::checkString($var, True);
        $this->condition = $var;

        return $this;
    }

}

// Adding a class alias for backwards compatibility with the previous class name.
class_alias(joinType::class, \OCA\Cloud_Py_API\Proto\DbSelectRequest_joinType::class);

