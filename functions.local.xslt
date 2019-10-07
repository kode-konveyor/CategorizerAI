<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xml>
<xsl:stylesheet
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version='2.0'
	xmlns:xhtml="http://www.w3.org/TR/xhtml1/transitional"
	xmlns:fn="http://www.w3.org/2005/xpath-functions"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:zenta="http://magwas.rulez.org/zenta">

	<xsl:output method="xml" version="1.0" encoding="utf-8"
		indent="yes" omit-xml-declaration="yes" />

	<!--xsl:template match="element[@xsi:type='Ada:varlistentry']" mode="elementTitle"> 
		<xsl:value-of select="@name"/> </xsl:template> <xsl:template match="element[@id='basicobject']|connection[@id='basicrelation']" 
		mode="varlistentry"> </xsl:template> <xsl:template match="folder[property[@key='display']/@value='hidden']" 
		mode="varlist"/ -->

    <xsl:function name="zenta:fullPackageName">
        <xsl:param name="doc"/>
        <xsl:param name="package"/>
        <xsl:for-each select="$package">
        <xsl:variable name="parent" select="zenta:neighbours($doc,.,'contains,2')"/>
        <xsl:value-of select="
            if(@xsi:type = 'Package')
            then
                if($parent/@xsi:type = 'Package')
                then
                    concat(string-join(zenta:fullPackageName($doc,$parent),''),'.',@name)
                else
                    @name
            else
                ''
        "/>
        </xsl:for-each>
    </xsl:function>

    <xsl:function name="zenta:artifactForBusinessObject">
        <xsl:param name="doc"/>
        <xsl:param name="object"/>
            <xsl:for-each select="zenta:neighbours($doc,$object,'has an example as/is an example of,1')">
            <artifact>
                <xsl:variable name="testData" select="zenta:neighbours($doc,.,'contains,2')[@xsi:type='TestData']"/>
                <xsl:copy-of select="@name"/>
                <xsl:attribute name="class" select="$testData/@name"/>
                <xsl:attribute name="package" select="zenta:fullPackageName($doc,zenta:neighbours($doc,$testData,'contains,2')[@xsi:type='Package'])"/>
            </artifact>
            </xsl:for-each>
    </xsl:function>

    <xsl:function name="zenta:gatherServices">
        <xsl:param name="doc"/>
		<xsl:for-each select="$doc//element[@xsi:type='Service']">
            <xsl:variable name="result" select="zenta:neighbours($doc,.,'results,1')"/>
            <service>
                <xsl:copy-of select="@name"/>
                <xsl:attribute name="type" select="$result/value[@ancestorName='is of/is type of']/@name"/>
                <xsl:attribute name="package" select="zenta:fullPackageName($doc,zenta:neighbours($doc,.,'is implemented by/implements,2;contains,2'))"/>
                <result>
                    <xsl:copy-of select="zenta:artifactForBusinessObject($doc,$result)"/>
                </result>
                <xsl:for-each select="zenta:neighbours($doc,.,'uses,1')">
                    <xsl:sort select="value[@ancestorName='referenced as/references']/@name"/>
                    <param>
                        <xsl:variable name="businessObject" select="zenta:neighbours($doc,.,'is/is used as parameter,1')"/>
                        <xsl:copy-of select="$businessObject/value[@ancestorName='is/is used as parameter']/@name"/>
                        <xsl:attribute name="type" select="$businessObject/value[@ancestorName='is of/is type of']/@name"/>
                        <xsl:copy-of select="zenta:artifactForBusinessObject($doc,$businessObject)"/>
                    </param>
                </xsl:for-each>
            </service>
		</xsl:for-each>
    </xsl:function>
</xsl:stylesheet>
